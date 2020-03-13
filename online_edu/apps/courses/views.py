from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import View
from pure_pagination import Paginator, PageNotAnInteger
from courses.models import Course, CourseResourse, Video
from operation.models import UserFavorite, CourseComments, UserCourse
from utils.mixin_utils import LoginRequiredMixin

class CourseListView(View):
    def get(self,request):
        all_courses = Course.objects.all().order_by('-add_time')

        hot_courses = Course.objects.all().order_by('-click_nums')[:3]

        #课程搜索
        search_keywords = request.GET.get('keywords','')
        if search_keywords:
            all_courses = all_courses.filter(Q(name__icontains=search_keywords) |
                                             Q(desc__icontains=search_keywords) |
                                             Q(detail__icontains=search_keywords))

        #课程排序
        sort = request.GET.get('sort', '')
        if sort:
            if sort == 'students':
                all_courses = all_courses.order_by('-students')
            elif sort == 'hot':
                all_courses = all_courses.order_by('-click_nums')
        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_courses, 3, request=request)

        courses = p.page(page)

        return render(request,'course-list.html',{
            'all_courses': courses,
            'sort': sort,
            'hot_courses': hot_courses,
        })

class CourseDetailView(View):
    """
    课程详情页
    """
    def get(self,request,course_id):
        course = Course.objects.get(id=int(course_id))
        course.click_nums += 1
        course.save()

        has_fav_course = False
        has_fav_org = False

        if request.user.is_authenticated:
            if UserFavorite.objects.filter(user=request.user, fav_id=course.id, fav_type=1):
                has_fav_course = True
            if UserFavorite.objects.filter(user=request.user, fav_id=course.course_org_id, fav_type=2):
                has_fav_org = True
        tag = course.tag
        if tag:
            relate_courses = Course.objects.filter(tag=tag)[:1]
        else:
            relate_courses = []
        return render(request,'course-detail.html',{
                'course':course,
                'relate_courses':relate_courses,
                'has_fav_course':has_fav_course,
                'has_fav_org':has_fav_org,
        })

class CourseInfoView(LoginRequiredMixin,View):
    def get(self,request,course_id):
        course = Course.objects.get(id=int(course_id))
        course.students += 1
        course.save()
        #查询用户是否已经关联了该课程
        user_courses = UserCourse.objects.filter(user = request.user,course=course)
        if not user_courses:
            user_course = UserCourse(user = request.user,course=course)
            user_course.save()
        user_courses = UserCourse.objects.filter(course=course)
        user_ids = [user_courses.user.id for user_courses in user_courses]
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
        #取出所有课程ID
        course_ids = [user_courses.course.id for user_courses in all_user_courses]
        #获取学过该用户学过其他的所有课程
        relate_courses = Course.objects.filter(id__in=course_ids).order_by("-click_nums")[:5]
        all_resources = CourseResourse.objects.filter(course=course)
        return render(request, 'course-video.html', {
            'course': course,
            'all_resources': all_resources,
            'relate_courses': relate_courses,

        })

class CommentsView(LoginRequiredMixin,View):
    def get(self,request,course_id):
        course = Course.objects.get(id=int(course_id))
        all_resources = CourseResourse.objects.filter(course=course)
        all_comments = CourseComments.objects.all()
        return render(request, 'course-comment.html', {
            'course': course,
            'all_resources': all_resources,
            'all_comments': all_comments,

        })

class AddCommentsView(View):
    """
    用户添加课程评论
    """
    def post(self,request):
        if not request.user.is_authenticated:
            return HttpResponse('{"status ":"fail","msg":"用户未登录"}', content_type='application/json')

        course_id = request.POST.get("course_id",0)
        comments = request.POST.get("comments","")
        if int(course_id)>0 and comments:
            course_comments = CourseComments()
            course = Course.objects.get(id=course_id)
            course_comments.course = course
            course_comments.comments = comments
            course_comments.user = request.user
            course_comments.save()
            return HttpResponse('{"status":"success","msg":"添加成功"}', content_type='application/json')
        else:
            return HttpResponse('{"status":"fail","msg":"添加失败"}', content_type='application/json')

class VideoPlayView(View):
    """
    课程视频播放页
    """
    def get(self, request, video_id):
        video = Video.objects.get(id=int(video_id))
        course = video.lesson.course
        course.students += 1
        course.save()
        # 查询用户是否已经关联了该课程
        user_courses = UserCourse.objects.filter(user=request.user, course=course)
        if not user_courses:
            user_course = UserCourse(user=request.user, course=course)
            user_course.save()
        user_courses = UserCourse.objects.filter(course=course)
        user_ids = [user_course.user.id for user_course in user_courses]
        all_user_courses = UserCourse.objects.filter(user_id__in=user_ids)
        # 取出所有课程ID
        course_ids = [user_courses.course.id for user_courses in all_user_courses]
        # 获取学过该用户学过其他的所有课程
        relate_courses = Course.objects.filter(id__in=course_ids).order_by("-click_nums")[:5]
        all_resources = CourseResourse.objects.filter(course=course)
        return render(request, 'course-play.html', {
            'video': video,
            'course': course,
            'all_resources': all_resources,
            'relate_courses': relate_courses,

        })


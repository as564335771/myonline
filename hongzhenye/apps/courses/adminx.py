# _*_ coding: utf-8 _*_
import xadmin
from apps.courses.models import Course, Lesson, Video, CourseResourse

__author__ = 'hzy'
__date__ = '2020/2/3 20:33'

class LessonInline(object):
    model = Lesson
    extra = 0

class CourseResourceInline(object):
    model = CourseResourse
    extra = 0

class CourseAdmin(object):
    list_display = ['name','desc','detail','degree','learn_times','fav_nums','image','click_nums','add_time']
    search_fields = ['name','desc','detail','degree','learn_times','fav_nums','image','click_nums']
    list_filter = ['name','desc','detail','degree','learn_times','fav_nums','image','click_nums','add_time']

    style_fields = {"detail": "ueditor"}
    inlines = [LessonInline,CourseResourceInline]

    ordering = ['-click_nums']
    readonly_fields = ['click_nums']
    exclude = ['fav_nums']
    list_editable = ['desc','name']
    refresh_times = [3]

    def queryset(self):
        # 重载queryset方法，来过滤我们的数据
        qs = super(CourseAdmin,self).queryset()
        # 只显示is_banner=True的课程
        qs = qs.filter(is_banner=True)
        return qs

    def save_models(self):
        # 保存课程同时统计课程机构的课程数
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()

class LessonAdmin(object):
    list_display = ['course','name','add_time']
    search_fields = ['course','name']
    list_filter = ['course','name','add_time']


class VideoAdmin(object):
    list_display = ['lesson','name','add_time']
    search_fields = ['lesson','name']
    list_filter = ['lesson','name','add_time']


class CourseResourseAdmin(object):
    list_display = ['course','name','download','add_time']
    search_fields = ['course','name','download']
    list_filter = ['course','name','download','add_time']


xadmin.site.register(Course,CourseAdmin)
xadmin.site.register(Lesson,LessonAdmin)
xadmin.site.register(Video,VideoAdmin)
xadmin.site.register(CourseResourse,CourseResourseAdmin)
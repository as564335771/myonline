# _*_ coding: utf-8 _*_
import xadmin
from apps.courses.models import Course, Lesson, Video, CourseResourse

__author__ = 'hzy'
__date__ = '2020/2/3 20:33'

class CourseAdmin(object):
    list_display = ['name','desc','detail','degree','learn_times','fav_nums','image','click_nums','add_time']
    search_fields = ['name','desc','detail','degree','learn_times','fav_nums','image','click_nums']
    list_filter = ['name','desc','detail','degree','learn_times','fav_nums','image','click_nums','add_time']


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
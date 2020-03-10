# _*_ coding: utf-8 _*_
from django.conf.urls import url
from django.urls import re_path


from apps.courses.views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddCommentsView, \
    VideoPlayView

__author__ = 'hzy'
__date__ = '2020/2/8 11:23'

app_name = 'course'
urlpatterns = [
    url(r'^list/$', CourseListView.as_view(), name='course_list'),
    #课程详情
    re_path(r'^detail/(?P<course_id>\d+)/', CourseDetailView.as_view(), name='course_detail'),
    re_path(r'^info/(?P<course_id>\d+)/', CourseInfoView.as_view(), name='course_info'),
    #课程评论
    re_path(r'^comments/(?P<course_id>\d+)/', CommentsView.as_view(), name='course_comment'),
    #添加评论
    re_path(r'^add_comment/$', AddCommentsView.as_view(), name='add_comment'),
    #课程视频播放页
    re_path(r'^video/(?P<video_id>\d+)/', VideoPlayView.as_view(), name='video_play'),

]
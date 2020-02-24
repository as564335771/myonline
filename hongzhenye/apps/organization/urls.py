# _*_ coding: utf-8 _*_
from django.conf.urls import url
from django.urls import re_path

from apps.organization.views import OrgView, AddUserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView, \
    TeacherListView, TeacherDetailView
from apps.organization.views import AddFavView

__author__ = 'hzy'
__date__ = '2020/2/8 11:23'

app_name = 'organization'
urlpatterns = [
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask'),
    re_path('home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name="org_home"),
    re_path('course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name="org_course"),
    re_path('desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name="org_desc"),
    re_path('org_teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name="org_teacher"),

    #机构收藏
    url('add_fav/$', AddFavView.as_view(), name="add_fav"),
    #讲师列表页
    url('teacher/list/$', TeacherListView.as_view(), name="teacher_list"),
    #讲师详情页
    re_path('teacher/detail/(?P<teacher_id>\d+)/$', TeacherDetailView.as_view(), name="teacher_detail"),

]
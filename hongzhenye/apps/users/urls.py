# _*_ coding: utf-8 _*_
from django.conf.urls import url
from django.urls import re_path

from users.views import UserinfoView, UploadImageView, UpdatePwdView, SendEmailCodeView, UpdateEmailView, MyCourseView, \
    MyFavOrgView, MyFavTeacherView, MyFavCourseView, MymessageView

__author__ = 'hzy'
__date__ = '2020/2/8 11:23'

app_name = 'users'
urlpatterns = [
    #用户信息
    url('info/$', UserinfoView.as_view(), name="user_info"),
    #用户头像上传
    url('image/upload/$', UploadImageView.as_view(), name="image_upload"),
    #用户个人中心修改密码
    url('update/pwd/$', UpdatePwdView.as_view(), name="update_pwd"),
    #发送邮箱验证码
    url('sendemail_code/$', SendEmailCodeView.as_view(), name="sendemail_code"),
    #修改邮箱
    url('update_email/$', UpdateEmailView.as_view(), name="update_email"),
     #我的课程
    url('mycourse/$', MyCourseView.as_view(), name="mycourse"),
    #我收藏的课程机构
    url('myfav/org/$', MyFavOrgView.as_view(), name="myfav_org"),
    #我收藏的教师
    url('myfav/teacher/$', MyFavTeacherView.as_view(), name="myfav_teacher"),
    #我收藏的课程
    url('myfav/course/$', MyFavCourseView.as_view(), name="myfav_course"),
    #我的消息
    url('mymessage/$', MymessageView.as_view(), name="mymessage"),



]
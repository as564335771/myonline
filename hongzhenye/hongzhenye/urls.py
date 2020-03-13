"""hongzhenye URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.static import serve

import xadmin
# from apps.organization.views import OrgView
from apps.users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView, \
    LogoutView, IndexView
from hongzhenye.settings import MEDIA_ROOT

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('xadmin/', xadmin.site.urls),
    url('^$',IndexView.as_view(),name='index'),
    url('^login/$', LoginView.as_view(), name='login'),
    url('^logout/$', LogoutView.as_view(), name='logout'),
    url('^register/$', RegisterView.as_view(), name='register'),
    url('^captcha/', include('captcha.urls')),
    url('^active/(?P<active_code>.*)/$', ActiveUserView.as_view(),name='user_active'),
    url('^forget/$', ForgetPwdView.as_view(),name='forget_pwd'),
    url('^reset/(?P<active_code>.*)/$', ResetView.as_view(), name='reset_pwd'),
    url('^modify_pwd/$', ModifyPwdView.as_view(), name='modify_pwd'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':MEDIA_ROOT}),
    # re_path(r'^static/(?P<path>.*)$', serve,{'document_root':STATIC_ROOT}),
    url('ueditor/', include('DjangoUeditor.urls')),

    #课程机构url配置
    url('^org/', include('organization.urls',namespace='org')),
    # 课程app相关url配置
    url('^course/', include('courses.urls', namespace='course')),
    # 课程 相关url配置
    url('^users/', include('users.urls', namespace='users')),
]
#全局404页面配置
handler404 = 'apps.users.views.page_not_found'
#全局500页面配置
handler500 = 'apps.users.views.page_error'

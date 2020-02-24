# _*_ coding: utf-8 _*_
import re

from django import forms

from apps.operation.models import UserAsk

__author__ = 'hzy'
__date__ = '2020/2/8 11:17'

# class UserAskForm(forms.Form):
#     name = forms.CharField(required=True,min_length=2,max_length=20)
#     phone = forms.CharField(required=True,min_length=11,max_length=11)
#     course_name = forms.CharField(required=True,min_length=5,max_length=5)

class UserAskForm(forms.ModelForm):

    class Meta:
        model = UserAsk
        fields = ['name','mobile','course_name']

    def clean_mobile(self):
        moblie = self.cleaned_data['mobile']
        REGEX_MOBILE = '^1[358]\d{9}$|^147\d{8}$|^176\d{8}$'
        p = re.compile(REGEX_MOBILE)
        if p.match(moblie):
            return moblie
        else:
            raise forms.ValidationError(u'手机号码非法',code = 'mobile_invalid')
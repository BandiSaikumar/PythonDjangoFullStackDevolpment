from django.conf.urls import url
from BasicApp import views

#Template Tagging
app_name = 'BasicApp'

urlpatterns = [
    url(r'^other/$',views.other,name='other'),
    url(r'^relative/$',views.relative,name='relative'),
]
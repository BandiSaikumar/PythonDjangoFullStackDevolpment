from django.conf.urls import url
from App2 import views

urlpatterns = [
    url(r'^$',views.users,name = 'users'),
    # url(r'^$',views.index,name = 'index'),
]
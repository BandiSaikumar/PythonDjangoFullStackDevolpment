from django.conf.urls import url
from App1 import views

urlpatterns = [
    url(r'^$',views.index,name = 'index'),
]
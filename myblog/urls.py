from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^index', views.blog_index),
    url(r'^(?P<id>\d+)',views.detail,name='detail'),
    url(r'^$',views.main_redirect)
]
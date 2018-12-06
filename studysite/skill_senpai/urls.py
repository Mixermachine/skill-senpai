from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.IndexView.as_view()),
    url(r'^api/query_lectures/$', views.query_lectures, name='query_lectures'),
]
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/query_lectures/$', views.query_lectures, name='query_lectures'),
    url(r'^lecture/(?P<pk>\d+)/$', views.LectureDetailView.as_view(), name='lecture-detail'),
]

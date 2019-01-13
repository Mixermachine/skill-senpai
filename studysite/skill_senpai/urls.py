from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.simpleProcessor, name='index'),
    url(r'^pre-lectures/$', views.simpleProcessor, name='pre-lectures'),
    url(r'^curriculum/$', views.simpleProcessor, name='curriculum'),
    url(r'contact/', views.simpleProcessor, name='contact'),
    url(r'^api/query_lectures/$', views.query_lectures, name='query_lectures'),
    url(r'^lecture/(?P<lecture_id>\w+)/$', views.LectureDetailView.as_view(), name='lecture-detail'),
]

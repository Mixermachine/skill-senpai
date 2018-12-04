from django.conf.urls import url
from skill_senpai.views import IndexView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/$', IndexView.as_view()),
]
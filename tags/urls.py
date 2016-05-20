from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^find_tags/', views.find_tags_profile, name='find_tags_profile'),
    url(r'^find_tags_profile/', views.find_tags, name='find_tags'),
    url(r'^add_tag/(?P<pk>\d+)/$', views.add_tag, name='add_tag'),
    url(r'^add_tag_profile/(?P<pk>\d+)/$', views.add_tag_profile, name='add_tag_profile'),
]

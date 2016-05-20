from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.my_profile, name='profile'),
    url(r'^edit/$', views.EditProfile.as_view(), name='edit_profile'),
    url(r'^(?P<pk>\d+)/$', views.their_profile, name='their_profile')
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.my_profile, name='profile'),
    url(r'^edit/$', views.EditProfile.as_view(), name='edit_profile')
]

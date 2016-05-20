from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.my_club, name='my_club'),
    url(r'^edit/$', views.EditClub.as_view(), name='edit_club'),
]

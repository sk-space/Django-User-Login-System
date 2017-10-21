from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.profile, name='index'),
    url(r'^edit/$', views.edit_user, name='edit')
]
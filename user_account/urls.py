from django.conf.urls import url
from . import views

app_name = 'user_account'


urlpatterns = [
	url(r'^register/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
   url(r'^login/$', views.login, name='login'),
   url(r'^logout/$', views.logout, name='logout'),
 ]


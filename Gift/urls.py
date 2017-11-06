from django.conf.urls import url, include
from django.contrib import admin
from customer import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.get_index, name='index'),


]

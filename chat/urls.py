from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.new_room, name='new_room'),
    url(r'^(?P<label>[\w-]{,50})/$', views.room, name='room'),
]

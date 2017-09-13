from django.conf.urls import include, url
from rest_framework.routers import SimpleRouter
from . import views
from .api import RoomViewSet
from .api import MessageViewSet


router = SimpleRouter()

router.register(r'room', RoomViewSet, base_name="room")
router.register(r'message', MessageViewSet, base_name="message")


urlpatterns = [
    url(r'^$',  views.about, name='about'),
    url(r'^app/$',  views.app, name='app'),
    url(r'^new/$', views.new_room, name='new_room'),
    url(r'^api/', include(router.urls)),
    url(r'^room/(?P<label>[\w-]{,50})/$', views.chat_room, name='chat_room'),
]

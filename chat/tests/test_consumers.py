import json

import pytest
from asgiref.inmemory import ChannelLayer as InMemoryChannelLayer
from channels import Group
from channels.handler import AsgiRequest
from channels.message import Message
from django.contrib.sessions.backends.file import SessionStore as FileSessionStore

from chat.consumers import ws_connect, ws_receive, ws_disconnect
from chat.models import Room

@pytest.fixture
def message_factory(settings, tmpdir):
    def factory(name, **content):
        channel_layer = InMemoryChannelLayer()
        message = Message(content, name, channel_layer)
        settings.SESSION_FILE_PATH = str(tmpdir)
        message.channel_session = FileSessionStore()
        return message
    return factory

@pytest.mark.django_db
def test_ws_connect(message_factory):
    r = Room.objects.create(label='room1')
    message = message_factory('test',
        path = b'/chat/room1',
        client = ['10.0.0.1', 12345],
        reply_channel = u'test-reply',
    )
    ws_connect(message)
    assert 'test-reply' in message.channel_layer._groups['chat-room1']
    assert message.channel_session['room'] == 'room1'

@pytest.mark.django_db
def test_ws_receive(message_factory):
    r = Room.objects.create(label='room1')
    message = message_factory('test', 
        text = json.dumps({'handle': 'H', 'message': 'M'})
    )

    # Normally this would happen when the person joins the room, but mock
    # it up manually here.
    message.channel_session['room'] = 'room1'
    Group('chat-room1', channel_layer=message.channel_layer).add(u'test-reply')

    ws_receive(message)

    _, reply = message.channel_layer.receive_many([u'test-reply'])
    reply = json.loads(reply['text'])
    assert reply['message'] == 'M'
    assert reply['handle'] == 'H'

@pytest.mark.django_db
def test_ws_disconnect(message_factory):
    r = Room.objects.create(label='room1')
    message = message_factory('test', reply_channel=u'test-reply1')
    Group('chat-room1', channel_layer=message.channel_layer).add(u'test-reply1')
    Group('chat-room1', channel_layer=message.channel_layer).add(u'test-reply2')
    message.channel_session['room'] = 'room1'

    ws_disconnect(message)
    assert 'test-reply1' not in message.channel_layer._groups['chat-room1']

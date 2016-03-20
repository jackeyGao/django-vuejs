import pytest
from asgiref.inmemory import ChannelLayer as InMemoryChannelLayer
from channels.handler import AsgiRequest
from channels.message import Message

from chat.consumers import ws_connect
from chat.models import Room

@pytest.fixture
def channel_layer():
    return InMemoryChannelLayer()

def make_message(channel_layer, name, **content):
    return Message(content, name, channel_layer)


# Ideally, I'd be able to test this without creating a Room, though that
# would make some modification/mocking to the consumer to make that work.
@pytest.mark.django_db
def test_ws_connect(channel_layer):
    r = Room.objects.create(label='room1')
    message = make_message(channel_layer, "test",
        path = '/chat/room1',
        client = '10.0.0.1:12345',
        reply_channel = 'test-reply',
    )
    ws_connect(message)
    assert 'test-reply' in message.channel_layer._groups['chat-room1']

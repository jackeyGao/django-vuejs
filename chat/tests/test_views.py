# Use django.test.TestCase here so I get the snazzy Django assertions.

from django.test import TestCase
from chat.models import Room

class ViewTests(TestCase):
    def test_about(self):
        r = self.client.get('/')
        self.assertTemplateUsed(r, 'chat/about.html')

    def test_new_room(self):
        r = self.client.get('/new/')
        room_label = r['Location'].strip('/')
        assert Room.objects.filter(label=room_label).exists()
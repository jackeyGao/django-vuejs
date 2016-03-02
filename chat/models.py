from __future__ import unicode_literals

import channels
from django.db import models
from django.utils import timezone

class Room(models.Model):
    label = models.SlugField(unique=True)

    def __unicode__(self):
        return self.label

    @property
    def channel_group(self):
        return channels.Group('chat-%s' % self.label)

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages')
    username = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now, db_index=True)

    def __unicode__(self):
        return '[{timestamp}] {username}: {message}'.format(**self.as_dict())

    @property
    def formatted_timestamp(self):
        return self.timestamp.strftime('%b %-d %-I:%M %p')
    
    def as_dict(self):
        return {'username': self.username, 'message': self.message, 'timestamp': self.formatted_timestamp}
from __future__ import unicode_literals

import datetime
from django.db import models

class Room(models.Model):
    label = models.SlugField(unique=True)

    def __unicode__(self):
        return self.label

class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages')
    username = models.TextField()
    message = models.TextField()
    timestamp = models.DateTimeField(default=datetime.datetime.now, db_index=True)

    def __unicode__(self):
        return '[{timestamp}] {username}: {message}'.format(
            timestamp = self.timestamp.strftime('%b %-d %-I:%M %p'),
            username = self.username,
            message = self.message
        )

    
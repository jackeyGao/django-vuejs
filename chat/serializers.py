from rest_framework import serializers
from chat.models import Room
from chat.models import Message


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name', 'label']


class MessageSerializer(serializers.ModelSerializer):
    timestamp = serializers.CharField(source="formatted_timestamp", read_only=True)

    class Meta:
        model = Message
        fields = ['room', 'handle', 'message', 'timestamp']

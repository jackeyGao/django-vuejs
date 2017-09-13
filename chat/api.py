import haikunator
from rest_framework import filters
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from chat.models import Room
from chat.models import Message
from chat.serializers import RoomSerializer
from chat.serializers import MessageSerializer


class RoomViewSet(mixins.CreateModelMixin, 
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def create(self, request, *args, **kwargs):
        new_room = None
        while not new_room:
            with transaction.atomic():
                label = haikunator.haikunate()
                if Room.objects.filter(label=label).exists():
                    continue
                new_room = Room.objects.create(label=label)

        serializer = self.get_serializer(new_room)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class MessageViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        label = self.request.query_params.get('label', None)
        limit = self.request.query_params.get('limit', 50)

        if label:
            queryset = Message.objects.filter(room__label=label)
        else:
            queryset = Message.objects.filter()

        return queryset[:int(limit)]

import random
import string
from django.db import transaction
from django.shortcuts import render, redirect
from .models import Room

def new_room(request):
    """
    Randomly create a new room, and redirect to it.
    """
    new_room = None
    while not new_room:
        with transaction.atomic():
            label = _generate_random_label(length=20)
            if Room.objects.filter(label=label).exists():
                continue
            new_room = Room.objects.create(label=label)
    return redirect(room, label=label)

def room(request, label):
    """
    Room view - show the room, with latest messages.

    The template for this view has the WebSocket business to send and stream
    messages, so see the template for where the magic happens.
    """
    # Automatically create new rooms just by hitting the URL.
    room, created = Room.objects.get_or_create(label=label)

    return render(request, "room.html", {
        'room': room,
        'messages': room.messages.order_by('-timestamp')[:100]
    })

def _generate_random_label(length):
    return "".join(random.choice(string.ascii_lowercase + string.digits) for i in range(length))
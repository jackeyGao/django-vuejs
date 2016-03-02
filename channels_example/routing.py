from channels.staticfiles import StaticFilesConsumer
from chat.consumers import ws_connect, ws_receive

channel_routing = {
    # This makes Django serve static files from settings.STATIC_URL, similar
    # to django.views.static.serve. This isn't ideal (not exactly production
    # quality) but it works for a minimal example.
    'http.request': StaticFilesConsumer(),

    'websocket.connect': ws_connect,
    'websocket.receive': ws_receive,
}
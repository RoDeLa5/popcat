from . import consumers

from django.urls import path

websocket_urlpatterns = [
    path('ws', consumers.PopcatConsumer.as_asgi())
]

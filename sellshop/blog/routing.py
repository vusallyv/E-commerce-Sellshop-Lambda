from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/blog/<slug:slug>/', consumers.ChatConsumer.as_asgi()),
]
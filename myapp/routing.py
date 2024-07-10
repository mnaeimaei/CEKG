# mydjangoapp/websocket/routing.py
from django.urls import re_path
from .consumers import ScriptProgressConsumer

websocket_urlpatterns = [
    re_path(r'ws/progress/$', ScriptProgressConsumer.as_asgi()),
]
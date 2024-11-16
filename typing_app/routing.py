from django.urls import path
from .consumers import TypingConsumer
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    path('ws/typing/', TypingConsumer.as_asgi()),
    re_path(r'ws/leaderboard/$', consumers.LeaderboardConsumer.as_asgi()),
]




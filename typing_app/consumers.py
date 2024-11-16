import json
from channels.generic.websocket import AsyncWebsocketConsumer

class TypingConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Handle messages here

        await self.send(text_data=json.dumps({
            'message': message
        }))

# your_app/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class LeaderboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("leaderboard_group", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("leaderboard_group", self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        # Process message

    async def send_leaderboard_data(self, data):
        await self.send(text_data=json.dumps({
            'leaderboard': data
        }))

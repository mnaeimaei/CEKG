import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ScriptProgressConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("progress_group", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("progress_group", self.channel_name)

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

    async def send_progress_update(self, progress):
        await self.send(text_data=json.dumps({
            'progress': progress
        }))

    # Handler for group messages
    async def progress_message(self, event):
        progress = event['progress']
        await self.send(text_data=json.dumps({
            'progress': progress
        }))

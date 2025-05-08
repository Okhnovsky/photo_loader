import json

from asgiref.sync import async_to_sync
from channels.exceptions import StopConsumer
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.layers import get_channel_layer


channel_layer = get_channel_layer()


class PhotoConsumer(AsyncWebsocketConsumer):
    """Потребитель для передачи ифнормации о необходимости обновления."""

    async def connect(self):
        self.group_name = "photo"

        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        raise StopConsumer()

    async def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        await self.send(text_data=json.dumps({"message": message}))


def update_photo():
    async_to_sync(channel_layer.group_send)(
        "photo",
        {"type": "chat_message", "message": "update"}
    )

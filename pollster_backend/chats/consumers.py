import asyncio

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Messages
from .serializers import MessagesSerializer

class ChatRoomConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = 'room_{}'.format(self.scope['url_route']['kwargs']['room_id'])
        self.room_group_name = 'chat_%s' % self.room_name

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive_json(self, content, **kwargs):
        message_type = content.get('type')
        if message_type == 'message.send':
            await self.create_message(content)
        elif message_type == 'message.update':
            await self.update_message(content)

    async def create_message(self, event):
        messages = await self._create_message(event.get('data'))
        
        await self.send_json({
            'type': 'MESSAGE',
            'data': messages.data,
            'action': 'create'
        })
    
    async def update_message(self, event):
        messages = await self._update_message(event.get('data'))

        await self.send_json({
            'type': 'MESSAGE',
            'data': messages.data,
            'action': 'update'
        })

    @database_sync_to_async
    def _create_message(self, content):
        serializer = MessagesSerializer(data=content)
        serializer.is_valid(raise_exception=True)
        messages = serializer.create(serializer.validated_data)
        return messages

    @database_sync_to_async
    def _update_message(self, content):
        instance = Messages.objects.get(id=content['id'])
        serializer = MessagesSerializer(data=content)
        serializer.is_valid(raise_exception=True)
        messages = serializer.update(instance, serializer.validated_data)
        return messages
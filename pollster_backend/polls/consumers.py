import asyncio

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Comments, Option
from .serializers import CommentsSerializer, OptionsSerializer

class PollsConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        self.room_name = 'poll_{}'.format(self.scope['url_route']['kwargs']['poll_id'])
        self.room_group_name = 'poll_series_%s' % self.room_name

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
        if message_type == 'comment.send':
            await self.create_comment(content)
        elif message_type == 'comment.update':
            await self.update_comment(content)
        elif message_type == 'poll.update':
            await self.update_option(content)

    async def create_comment(self, event):
        comment = await self._create_comment(event.get('data'))
        
        await self.send_json({
            'type': 'MESSAGE',
            'data': comment.data,
            'action': 'create'
        })
    
    async def update_comment(self, event):
        comment = await self._update_comment(event.get('data'))

        await self.send_json({
            'type': 'MESSAGE',
            'data': comment.data,
            'action': 'update'
        })

    async def update_option(self, event):
        option = await self._update_option(event.get('data'))

        await self.send_json({
            'type': 'MESSAGE',
            'data': option.data,
            'action': 'update'
        })

    @database_sync_to_async
    def _create_comment(self, content):
        serializer = MessagesSerializer(data=content)
        serializer.is_valid(raise_exception=True)
        comments = serializer.create(serializer.validated_data)
        return comments

    @database_sync_to_async
    def _update_comment(self, content):
        instance = Comments.objects.get(id=content['id'])
        serializer = CommentsSerializer(data=content)
        serializer.is_valid(raise_exception=True)
        comments = serializer.update(instance, serializer.validated_data)
        return comments
    
    @database_sync_to_async
    def _update_option(self, content):
        instance = Option.objects.get(id=content['id'])
        serializer = OptionsSerializer(data=content)
        serializer.is_valid(raise_exception=True)
        options = serializer.update(instance, serializer.validated_data)
        return options
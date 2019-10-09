import json

from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from .serializers import ChatRoomSerializer

class ChatRoomConsumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        self.room_name = self.scope['url_route']
        await self.accept()

    async def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        self.send(text_data=json.dumps({
            'message': message
        }))

    # async def receive_json(self, content, **kwargs):
    #     message_type = content.get('type')
    #     if message_type == 'create.trip':
    #         await self.create_trip(content)

    # # new
    # async def create_chat_room(self, event):
    #     chat_room = await self._create_trip(event.get('data'))
    #     await self.send_json({
    #         'type': 'MESSAGE',
    #         'data': chat_rooom
    #     })

    # # new
    # @database_sync_to_async
    # def _create_chat_room(self, content):
    #     serializer = ChatRoomSerializer(data=content)
    #     serializer.is_valid(raise_exception=True)
    #     chat_room = serializer.create(serializer.validated_data)
    #     return chat_room

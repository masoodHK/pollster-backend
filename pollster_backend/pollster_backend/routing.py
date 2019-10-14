from django.urls import path
from channels.auth import AuthMiddlewareStack  # new
from channels.routing import ProtocolTypeRouter, URLRouter  # changed

import chats.consumers
import polls.consumers

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/chats/<int:room_id>', chats.consumers.ChatRoomConsumer),
            path('ws/polls/<int:poll_id>', polls.consumers.PollsConsumer)
        ])
    )
})
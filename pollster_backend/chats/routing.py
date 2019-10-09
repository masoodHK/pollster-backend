from channels.auth import AuthMiddlewareStack  # new
from channels.routing import ProtocolTypeRouter, URLRouter  # changed

from .consumers import ChatRoomConsumer

# changed
application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('', ChatRoomConsumer),
        ])
    )
})
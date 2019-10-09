from django.urls import path

from .views import ChatRoomRUDView, ChatRoomView, MessagesView, MessagesRUDView

urlpatterns = [
    path('', ChatRoomView.as_view()),
    path('<int:pk>', ChatRoomRUDView.as_view()),
    path('<int:chat_id>/messages', MessagesView.as_view()),
    path('<int:chat_id>/messages/<int:pk>', MessagesRUDView.as_view())
]
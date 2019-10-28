from django.db import models
from django.contrib.auth import get_user_model

from polls.models import Poll

# Create your models here.
class ChatRoom(models.Model):
    class Meta:
        verbose_name_plural = "Chat Rooms"

    has_multiple_people = models.BooleanField(default=True)
    chat_name = models.TextField("Name of the Chat Room", null=True, unique=True, max_length=500)
    users = models.ManyToManyField(get_user_model())
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.chat_name
    

class Messages(models.Model):
    class Meta:
        verbose_name_plural = "Messages"
        
    chat = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    message = models.CharField("The message sent", max_length=500)
    sent_at = models.DateTimeField(auto_now_add=True)
    sent_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.message
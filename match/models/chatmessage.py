from django.db import models
from match.models.chatroom import ChatRoom
from match.models.userinfo import UserInfo


class ChatMessage(models.Model):
    chat_room = models.ForeignKey(ChatRoom, on_delete=False, related_name="message_roomid")
    user = models.ForeignKey(UserInfo, on_delete=False, related_name="message_userid")
    message = models.CharField(max_length=500)
    objects = models.Manager
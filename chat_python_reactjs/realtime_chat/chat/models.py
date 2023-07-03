from django.db import models
import uuid
class Message(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sender_id = models.TextField(max_length=255)
    receiver_id = models.TextField(max_length=255)

class ChatGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    members = models.JSONField(default=list)

    def add_member(self, user_id):
        self.members.append(user_id)
        self.save()

    def remove_member(self, user_id):
        self.members.remove(user_id)
        self.save()


class ChatMessageGroup(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    group = models.ForeignKey(ChatGroup, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sender_id = models.UUIDField(default=uuid.uuid4, editable=False)

    
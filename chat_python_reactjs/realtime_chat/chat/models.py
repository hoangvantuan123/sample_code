from django.db import models

class Message(models.Model):
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sender_id = models.TextField(max_length=255)
    receiver_id = models.TextField(max_length=255)

class ChatGroup(models.Model):
    name = models.CharField(max_length=255)
    members = models.JSONField(default=list)

    def add_member(self, user_id):
        user = ChatGroup.objects.get(id=user_id)
        self.members.add(user)

    def remove_member(self, user_id):
        user = ChatGroup.objects.get(id=user_id)
        self.members.remove(user)


class ChatMessageGroup(models.Model):
    group = models.ForeignKey(ChatGroup, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    sender_id = models.TextField(max_length=255)
    
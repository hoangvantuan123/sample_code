import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import *

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = 'chat_room'
        self.room_group_name = f'chat_{self.room_name}'

        # Kết nối vào nhóm phòng chat
        async_to_sync(self.channel_layer.group_add)(self.room_group_name, self.channel_name)

        self.accept()

    def disconnect(self, close_code):
        # Rời khỏi nhóm phòng chat
        async_to_sync(self.channel_layer.group_discard)(self.room_group_name, self.channel_name)

    def receive(self, text_data):
        data = json.loads(text_data)
        text = data['text']
        sender_id = data['sender_id']
        receiver_id = data['receiver_id']

        # Tạo tin nhắn và gửi đến nhóm phòng chat
        message = Message.objects.create(text=text, sender_id= sender_id , receiver_id = receiver_id)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': {
                    'id': message.id,
                    'text': message.text,
                    'sender_id': message.sender_id,
                    'receiver_id': message.receiver_id,
                    'created_at': message.created_at.isoformat(),
                }
            }
        )

    def chat_message(self, event):
        # Gửi tin nhắn tới WebSocket
        self.send(text_data=json.dumps(event['message']))


################################################################
class ChatGroupConsumer(WebsocketConsumer):
    async def connect(self):
        self.group_id = self.scope['url_route']['kwargs']['group_id']
        self.group_name = 'chat_%s' % self.group_id

        # Join group
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        sender_id = data['sender_id']

        # Save the message to the database
        chat_message_group = ChatMessageGroup.objects.create(
            group_id=self.group_id,
            text=message,
            sender_id=sender_id
        )

        # Send the message to the group
        await self.channel_layer.group_send(
            self.group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender_id': sender_id
            }
        )

    async def chat_message(self, event):
        message = event['message']
        sender_id = event['sender_id']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender_id': sender_id
        }))
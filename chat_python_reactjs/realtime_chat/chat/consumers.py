import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Message

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

        # Tạo tin nhắn và gửi đến nhóm phòng chat
        message = Message.objects.create(text=text)
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': {
                    'id': message.id,
                    'text': message.text,
                    'created_at': message.created_at.isoformat(),
                }
            }
        )

    def chat_message(self, event):
        # Gửi tin nhắn tới WebSocket
        self.send(text_data=json.dumps(event['message']))

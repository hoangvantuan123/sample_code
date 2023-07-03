from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.shortcuts import get_object_or_404
@csrf_exempt
def message_list(request):
    if request.method == 'GET':
        messages = Message.objects.all().order_by('created_at')
        data = [{'text': message.text, 'created_at': message.created_at, 'sender_id': message.sender_id, 'receiver_id': message.receiver_id} for message in messages]
        return JsonResponse(data, safe=False)

    elif request.method == 'POST':
        text = request.POST.get('text')
        sender_id = request.POST.get('sender_id')
        receiver_id = request.POST.get('receiver_id')
        
        if text is not None and sender_id is not None and receiver_id is not None:
            message = Message.objects.create(text=text, sender_id=sender_id, receiver_id=receiver_id)
            return JsonResponse({'id': message.id, 'text': message.text, 'created_at': message.created_at, 'sender_id': message.sender_id, 'receiver_id': message.receiver_id})
        else:
            return JsonResponse({'error': 'Invalid data provided'})
        


@async_to_sync
async def send_message_to_group(group_name, message, sender_id):
    channel_layer = get_channel_layer()
    await channel_layer.group_send(
        group_name,
        {
            'type': 'chat_message',
            'message': message,
            'sender_id': sender_id
        }
    )   
@api_view(['GET', 'POST'])
def send_message(request, group_id):
    if request.method == 'GET':
        # Handle GET request to retrieve messages from the group
        group = get_object_or_404(ChatGroup, id=group_id)
        messages = ChatMessageGroup.objects.filter(group=group)

        # Convert messages to JSON or perform other desired operations
        serialized_messages = [{'text': message.text, 'sender_id': message.sender_id} for message in messages]
        return Response(serialized_messages)
    elif request.method == 'POST':
        # Handle POST request to send a new message to the group
        group = get_object_or_404(ChatGroup, id=group_id)
        message = request.data['message']
        sender_id = request.data['sender_id']

        # Save the message to the database
        chat_message_group = ChatMessageGroup.objects.create(
            group=group,
            text=message,
            sender_id=sender_id
        )

        # Send the message to the group
        send_message_to_group('chat_%s' % group_id, message, sender_id)

        return Response({'status': 'success'})

@api_view(['GET', 'POST'])
def create_group(request):
    if request.method == 'GET':
        # Handle GET request to retrieve existing groups
        groups = ChatGroup.objects.all()
        serialized_groups = [{'id': group.id, 'name': group.name} for group in groups]
        return Response(serialized_groups)
    elif request.method == 'POST':
        # Handle POST request to create a new group
        name = request.data['name']
        members = request.data.get('members', [])

        group = ChatGroup.objects.create(name=name, members=members)

        return Response({'status': 'success'})

@api_view(['GET', 'POST'])
def add_member(request, group_id):
    try:
        group = ChatGroup.objects.get(id=group_id)
    except ChatGroup.DoesNotExist:
        return Response({'error': 'ChatGroup not found'}, status=404)

    if request.method == 'GET':
         # Xử lý yêu cầu GET để lấy danh sách thành viên trong nhóm
        members = group.members
        serialized_members = [{'id': member, 'name': f'Thành viên {member}'} for member in members]
        return Response(serialized_members)
    
    elif request.method == 'POST':
         # Xử lý yêu cầu POST để thêm thành viên mới vào nhóm
        member_id = request.data.get('member_id')
        if member_id is None:
            return Response({'error': 'Missing member_id'}, status=400)

         # Kiểm tra xem member_id đã tồn tại trong nhóm chưa
        if member_id in group.members:
            return Response({'error': 'Member already exists in the group'}, status=400)

        # Trích xuất giá trị JSON, thêm thành viên mới và lưu trở lại
        members = group.members
        members.append(member_id)
        group.members = members
        group.save()

        return Response({'status': 'success'})

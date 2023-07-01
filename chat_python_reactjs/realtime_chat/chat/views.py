from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Message

@csrf_exempt
def message_list(request):
    if request.method == 'GET':
        messages = Message.objects.all().order_by('created_at')
        data = [{'text': message.text, 'created_at': message.created_at} for message in messages]
        return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':
        text = request.POST.get('text', '')
        message = Message.objects.create(text=text)
        return JsonResponse({'id': message.id, 'text': message.text, 'created_at': message.created_at})

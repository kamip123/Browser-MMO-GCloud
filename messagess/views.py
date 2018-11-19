from django.shortcuts import render
from django.utils import timezone
from .models import Message
from .forms import sendMessageForm
# Create your views here.


def messages_page(request):
    messages = Message.objects.filter(toWho=request.user).order_by('created_date')
    return render(request, 'indexMessagess.html', {'messages': messages})


def messages_detail_page(request, idOfMessage):
    message = Message.objects.get(id=idOfMessage)
    return render(request, 'messagessDetail.html', {'message': message})

def messages_your_send_page(request):
    messages = Message.objects.filter(author=request.user).order_by('created_date')
    return render(request, 'messagessYourSend.html', {'messages': messages})

def messages_send_page(request):
    user = request.user
    if request.method == 'POST':
        messageFormReceived = sendMessageForm(request.POST)
        if messageFormReceived.is_valid():
            message = messageFormReceived.save(commit=False)
            message.author = user
            message.save()
        else:
            return render(request, 'messagessSend.html', {'messageForm': messageFormReceived})
    messageForm = sendMessageForm()
    return render(request, 'messagessSend.html', {'messageForm': messageForm})

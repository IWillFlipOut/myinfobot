from django.shortcuts import render
from .models import Chatbot

def chatbot_view(request):
    chatbots = Chatbot.objects.all()
    return render(request, 'chatbot.html', {'chatbots': chatbots})

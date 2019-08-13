from django.shortcuts import render
from .models import Question,Choice
# Create your views here.

def index(request):
    questions=Question.objects.order_by('-id')
    return render(request,'questions/Questionare.html',{"questions":questions})
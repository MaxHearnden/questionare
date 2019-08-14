from django.shortcuts import render
from .models import Question,Choice,Response,Answer
# Create your views here.
from django.utils import timezone
def index(request):
    questions=Question.objects.order_by('-id')
    return render(request,'questions/Questionare.html',{"questions":questions})

def submit(request):
    response=Response(date_done=timezone.now())
    response.save()
    questions=Question.objects.order_by('-id')
    for i in questions:
        answer=response.answer_set.create(answer=request.POST[i.name],question=i)
        answer.save()
    return render(request,'questions/feedback.html')
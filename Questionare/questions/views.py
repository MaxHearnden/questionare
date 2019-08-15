import csv
from django.http import HttpResponse
from django.shortcuts import render
from .models import Page,Question,Choice,Response,Answer
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.utils import timezone
def index(request):
    newresponse=Response(date_done=timezone.now())
    newresponse.save()
    request.session["response no"]=newresponse.id
    request.session["page no"]=1
#    questions=Page.objects.get(pk=1).question_set.order_by('-id')
#    return render(request,'questions/Questionare.html',{"questions":questions,})
    return form(request)

def form(request):
    page=Page.objects.get(pk=request.session["page no"])
    questions=page.question_set.order_by('-id').order_by('-order')
    return render(request,'questions/Questionare.html',{"questions":questions,})

def submit(request):
#    response=Response(date_done=timezone.now())
#    response.save()
    response=Response.objects.get(pk=request.session["response no"])
    page=Page.objects.get(id=request.session["page no"])
    questions=Question.objects.filter(page=page)
    for i in questions:
        if i in questions:
            answer=response.answer_set.create(answer=request.POST[i.name],question=i)
            answer.save()
    return render(request,'questions/feedback.html')

@login_required
def data(request):
    data=[[]]
    for i in Response.objects.all():
        response=['']*len(data[0])
        for j in i.answer_set.all():
            if j.question.name not in data[0]:
                data[0].append(j.question.name)
                response.append([''])
            response[data[0].index(j.question.name)]=j.answer
        data.append(response)
    httpresponse=HttpResponse(content_type='text/csv')
    writer=csv.writer(httpresponse)
    writer.writerows(data)
    return httpresponse
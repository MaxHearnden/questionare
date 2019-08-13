from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'questions/index.html')

def trap(request,path):
    return render(request,'house_trapped/'+path)
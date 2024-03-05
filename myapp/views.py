from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  """  return HttpResponse("Hey There You are Connected with the django server")  """
  return render(request, 'index.html')

def new(request):
    return HttpResponse("New Function") 

def home(request):
   return render(request, 'home.html')

def res(request):
   return render(request,'res.html')

def new_file(request):
   return render(request,'new_file.html')

def task(request):
   return render(request,'task.html')

def task1(request):
   return render(request,'task1.html')

def task2(request):
   return render(request,'task2.html')

def task3(request):
   return render(request,'task3.html')

def task4(request):
   return render(request,'task4.html')
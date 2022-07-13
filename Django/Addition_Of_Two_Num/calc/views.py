from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request,'home.html')

def add(request):
       num1 = int(request.GET["num1"])
       num2 = int(request.GET["num2"])
       res = num1 + num2
       
       return render(request,'index.html', {"result":res} )     

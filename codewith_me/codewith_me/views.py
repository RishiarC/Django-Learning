from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Welcome to CodeWithMe!")
    return render(request,'index.html')

def about(request):
    return HttpResponse("tume ab kar sakte ho djnago !")

def contact(request):
    return HttpResponse("Welcome to in your life!")
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello, welcome to my django project")
def home(request):
    return render(request,"home.html")
def about(request):
    return render(request,"about.html")

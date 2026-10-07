from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def landing(request):
    return HttpResponse('<div style="color: green;text-align:center"><h1>Welcome to my first django project</h1></div>')
def home(request):
    return render(request,"home.html",{
        "name":" home page of my django project"
    })
def about(request):
    return HttpResponse('<div style="color: blue;text-align:center"><h1>This is the about page of my project</h1></div>')
def main(request):
    return render(request,"main.html",{
        "name":"Main page of my project which contains dashboards for my project"
    })
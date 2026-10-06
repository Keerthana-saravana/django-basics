from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def home(request):
    return HttpResponse("<h1>welcome to django</h1>")

def main(request):
    return HttpResponse("""
<div style="
width:600px;
height:50px;
margin:80px auto;
padding:40px;
text-align:center;
background-color:yellow;
border-radius:10px;

">
<h1 style="color:green;">this is the main page</h1>
</div>

    """)
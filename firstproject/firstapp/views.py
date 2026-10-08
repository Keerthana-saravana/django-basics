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

student_list = [
    {
        "id": 1,
        "name": "Arun",
        "age": 20,
        "mark": 85
    },
    {
        "id": 2,
        "name": "Priya",
        "age": 21,
        "mark": 45
    },
    {
        "id": 3,
        "name": "Karthik",
        "age": 20,
        "mark": 72
    },
    {
        "id": 4,
        "name": "Divya",
        "age": 22,
        "mark": 35
    }
]
def students(request):
    return render(request,"students.html",{
        "students":student_list
    })
def student_details(request,id):
    for student in student_list:
        if student["id"]==id:
            return render(request,"details.html",{
                "student":student
            })

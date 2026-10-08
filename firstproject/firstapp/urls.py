from django.urls import path
from.import views

urlpatterns=[
    path('',views.students,name='students'),
    path('student/<int:id>/',views.student_details,name="student_details"),
    path('about/',views.about,name='about'),
    path('main/',views.main,name='main'),
    path('home/',views.home,name='home')
    
]
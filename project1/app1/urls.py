from django.urls import path,include
from.import views

urlpatterns=[
    path('demo',views.index,name="index"),
    path('',views.home,name="home"),
    path('about/',views.about,name="about")
]
"""Myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from .views import UserAPIView,UserDetails,MentorAPIView,MentorDetails,ProjectAPIView,ProjectToUserAPI,ProjectToMentorAPI,UserToProject,MenteesOfMentor,ProjectOfMnetor,MnetorMenteeOfPrject

urlpatterns = [
    # path('user/', user_list),
    path('user/', UserAPIView.as_view()),
    path('user/<int:pk>/',UserDetails.as_view()),
    path('mentor/', MentorAPIView.as_view()),
    path('mentor/<int:pk>/',MentorDetails.as_view()),
    path('project/', ProjectAPIView.as_view()),
    path('project/<int:pk>/user',ProjectToUserAPI.as_view()),
    path('project/<int:pk>/mentor',ProjectToMentorAPI.as_view()),
    path('user/<int:pk>/project',UserToProject.as_view()),
    path('mentor/<int:pk>/mentees',MenteesOfMentor.as_view()),
    path('mentor/<int:pk>/project',ProjectOfMnetor.as_view()),
    path('project/<int:pk>/mentor/mentees',MnetorMenteeOfPrject.as_view())
]

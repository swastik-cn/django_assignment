from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import User,Mentor,Project
from .serializers import UserSerializer, MentorSerializer,ProjectSerializer,ProjectSerializer1,ProjectSerializer2,ProjectSerializer3,ProjectSerializer4,ProjectSerializer5
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from drf_yasg.openapi import SwaggerDict 

class UserAPIView(APIView):
    def get(self,request):
        """
        returns a list of all users
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    @swagger_auto_schema(request_body=UserSerializer)
    def post(self,request):
        """
        creates a new user
        """
        serializer = UserSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
class UserDetails(APIView):
    def get_object(self,pk):
        try:
            print(pk)
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,pk):
        """
        gets the user with given id
        """
        user= self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    @swagger_auto_schema(request_body=UserSerializer)
    def put(self,request,pk):
        """
        modifies the user with given id
        """
        user= self.get_object(pk)
        serializer = UserSerializer(user,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )
    def delete(self,request,pk):
        """
        deletes the user with the given id
        """
        user= self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class MentorAPIView(APIView):
    def get(self,request):
        """
        gets all the mentors
        """
        Mentors = Mentor.objects.all()
        serializer = MentorSerializer(Mentors, many=True)
        return Response(serializer.data)
    @swagger_auto_schema(request_body=MentorSerializer)
    def post(self,request):
        """
        creates a new mentor
        """
        serializer = MentorSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
class MentorDetails(APIView):
    def get_object(self,pk):
        try:
            print(pk)
            return Mentor.objects.get(pk=pk)
        except Mentor.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,pk):
        """
        insert id of mentor to get details of the mentor
        """
        Mentor= self.get_object(pk)
        serializer = MentorSerializer(Mentor)
        return Response(serializer.data)
    @swagger_auto_schema(request_body=MentorSerializer)
    def put(self,request,pk):
        """
        modifies the mentor with given id
        """
        Mentor= self.get_object(pk)
        serializer = MentorSerializer(Mentor,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )
    def delete(self,request,pk):
        """
        deletes a mentor with given id
        """
        Mentor= self.get_object(pk)
        Mentor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class ProjectAPIView(APIView):
    def get(self,request):
        """
        gets all the projects
        """
        Projects = Project.objects.all()
        serializer = ProjectSerializer(Projects, many=True)
        return Response(serializer.data)
    @swagger_auto_schema(request_body=ProjectSerializer2)
    def post(self,request):
        """
        adds a new project
        """
        serializer = ProjectSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
class ProjectToUserAPI(APIView):
    def get_project_object(self,pk):
        try:
            print(pk)
            return Project.objects.get(project_id=pk)
        except Project.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def get_user_object(self,pk):
        try:
            print(pk)
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    # def get(self,request,pk):
    #     project= self.get_project_object(pk)
    #     print(request.data)
    #     serializer = ProjectSerializer(project)
    #     return Response(serializer.data)
    @swagger_auto_schema(request_body=ProjectSerializer4)
    def patch(self,request,pk):
        """
        assignes the list of mentees to the project 
        insert project id in id 
        and ids of mentees in the JSON list
        """
        project= self.get_project_object(pk)
        print(request.data)
        for i in request.data["mentees"]:
            user=self.get_user_object(i)
            project.mentees.add(user)

        project.save()
        # return project
        return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)
    
class ProjectToMentorAPI(APIView):
    def get_project_object(self,pk):
        try:
            print(pk)
            return Project.objects.get(project_id=pk)
        except Project.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def get_mentor_object(self,pk):
        try:
            print(pk)
            return Mentor.objects.get(pk=pk)
        except Mentor.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    # def get(self,request,pk):
    #     project= self.get_project_object(pk)
    #     print(request.data)
    #     serializer = ProjectSerializer(project)
    #     return Response(serializer.data)
    @swagger_auto_schema(request_body=ProjectSerializer3)
    def patch(self,request,pk):
        """
        assignes  mentor to the project 
        insert project id in id 
        and id of mentor in the JSON 
        """
        project= self.get_project_object(pk)
        mentor = self.get_mentor_object(request.data['mentor'])
        project.mentor=mentor
        project.save()
        # serializer = ProjectSerializer(data= request.data)
        return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)

class UserToProject(APIView):
    def get_project_object(self,pk):
        try:
            print(pk)
            return Project.objects.get(project_id=pk)
        except Project.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def get_user_object(self,pk):
        try:
            print(pk)
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    # def get(self,request,pk):
    #     user=self.get_user_object(pk)
    #     print(request.data)
    #     serializer = UserSerializer(user)
    #     return Response(serializer.data)
    @swagger_auto_schema(request_body=ProjectSerializer5)
    def patch(self,request,pk):
        """
        assignes project to a user
        insert user's mentee id in the id
        and project id in the json
        """
        user=self.get_user_object(pk)
        project= self.get_project_object(request.data['project_id'])
        project.mentees.add(user)
        project.save()
        # return project
        return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)

class MenteesOfMentor(APIView):
    """
    Gets all the mentees under a mentor 
    Insert id if mentor in id
    """
    def get_project_object(self,pk):
        try:
            print(pk)
            return Project.objects.get(project_id=pk)
        except Project.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def get_user_object(self,pk):
        try:
            print(pk)
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def get_mentor_object(self,pk):
        try:
            print(pk)
            return Mentor.objects.get(pk=pk)
        except Mentor.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,pk):
        mentor=self.get_mentor_object(pk)
        project= Project.objects.all()
        project= project.filter(mentor=mentor)
        serializer = ProjectSerializer(project,many=True)
        se=set()
        li=[]
        
        for i in serializer.data:
            for j in i['mentees']:
                if j not in se:
                    print(UserSerializer(self.get_user_object(j)).data)
                    li.append(UserSerializer(self.get_user_object(j)).data)
                    se.add(j)
        return Response(li)

        

class ProjectOfMnetor(APIView):
    """
    Gets all the projects under a mentor 
    Insert id if mentor in id
    """
    def get_project_object(self,pk):
        try:
            print(pk)
            return Project.objects.get(project_id=pk)
        except Project.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def get_mentor_object(self,pk):
        try:
            print(pk)
            return Mentor.objects.get(pk=pk)
        except Mentor.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,pk):
        mentor=self.get_mentor_object(pk)
        project= Project.objects.all()
        project= project.filter(mentor=mentor)
        serializer = ProjectSerializer(project,many=True)
        return Response(serializer.data)

class MnetorMenteeOfPrject(APIView):
    """
    Gets all the mentees and mentor  of project
    Insert project id in id
    """
    def get_project_object(self,pk):
        try:
            print(pk)
            return Project.objects.get(project_id=pk)
        except Project.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)
    def get(self,request,pk):
        project= self.get_project_object(pk)
        serializer = ProjectSerializer1(project)
        return Response(serializer.data)
    

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import User,Mentor,Project
from .serializers import UserSerializer, MentorSerializer,ProjectSerializer,ProjectSerializer1
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class UserAPIView(APIView):
    """
    get returns the list of users
    and post creates a user
    """
    def get(self,request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    def post(self,request):
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
        user= self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    def put(self,request,pk):
        # data = JSONParser().parse(request)
        user= self.get_object(pk)
        serializer = UserSerializer(user,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )
    def delete(self,request,pk):
        user= self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class MentorAPIView(APIView):
    """
    get returns the list of Mentors
    and post creates a Mentor
    """
    def get(self,request):
        Mentors = Mentor.objects.all()
        serializer = MentorSerializer(Mentors, many=True)
        return Response(serializer.data)
    def post(self,request):
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
        Mentor= self.get_object(pk)
        serializer = MentorSerializer(Mentor)
        return Response(serializer.data)
    def put(self,request,pk):
        Mentor= self.get_object(pk)
        serializer = MentorSerializer(Mentor,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )
    def delete(self,request,pk):
        Mentor= self.get_object(pk)
        Mentor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class ProjectAPIView(APIView):
    """
    get returns the list of Projects
    and post creates a Project
    """
    def get(self,request):
        Projects = Project.objects.all()
        serializer = ProjectSerializer(Projects, many=True)
        return Response(serializer.data)
    def post(self,request):
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
    def get(self,request,pk):
        project= self.get_project_object(pk)
        print(request.data)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    def patch(self,request,pk):
        project= self.get_project_object(pk)
        print(request.data)
        for i in request.data:
            user=self.get_user_object(i['User'])
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
    def get(self,request,pk):
        project= self.get_project_object(pk)
        print(request.data)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    def patch(self,request,pk):
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
    def get(self,request,pk):
        user=self.get_user_object(pk)
        print(request.data)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    def patch(self,request,pk):
        user=self.get_user_object(pk)
        project= self.get_project_object(request.data['project'])
        project.mentees.add(user)
        project.save()
        # return project
        return Response(ProjectSerializer(project).data, status=status.HTTP_201_CREATED)

class MenteesOfMentor(APIView):
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
    

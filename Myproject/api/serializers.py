from rest_framework import serializers
from .models import User,Mentor,Project

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields= '__all__'
class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields= '__all__'
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields= '__all__'
class ProjectSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields= ['mentor','mentees']
class ProjectSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields= ['name']
class ProjectSerializer3(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields= ['mentor']
class ProjectSerializer4(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields= ['mentees']

class ProjectSerializer5(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields= ['project_id']
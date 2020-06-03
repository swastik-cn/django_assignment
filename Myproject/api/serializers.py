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


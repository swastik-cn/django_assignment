from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=1000)
    user_id = serializers.IntegerField()
    def create(self,validated_data):
        return User.objects.create(validated_data)
    def update(self,instance,validated_data):
        instance.name=validated_data.get('name',instance.name)

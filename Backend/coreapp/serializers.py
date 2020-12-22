from rest_framework import serializers
from .models import Friends
from django.contrib.auth import get_user_model
User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name','last_name']

class PostSerializer(serializers.ModelSerializer):
    from_username = UserSerializer()
    class Meta:
        model= Friends
        fields = [
            'from_username'
        ]



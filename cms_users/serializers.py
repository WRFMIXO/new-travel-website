from rest_framework import serializers
from .models import AppUsers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppUsers
        fields = '__all__'


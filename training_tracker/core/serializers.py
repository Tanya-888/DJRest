from rest_framework import serializers
from .models import WorkoutProgram, User

class WorkoutProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutProgram
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'role')
from rest_framework import serializers
from .models import (
    User,
    CoachProfile,
    WorkoutProgram,
    Exercise,
    UserWorkoutPlan,
    ExerciseResult,
    Reminder
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CoachProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoachProfile
        fields = '__all__'

class WorkoutProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutProgram
        fields = '__all__'

class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = '__all__'

class UserWorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWorkoutPlan
        fields = '__all__'

class ExerciseResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseResult
        fields = '__all__'

class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reminder
        fields = '__all__'
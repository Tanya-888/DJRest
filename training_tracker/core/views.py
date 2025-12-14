# core/views.py
from rest_framework import generics
from .models import WorkoutProgram
from .serializers import WorkoutProgramSerializer

class PublicWorkoutPrograms(generics.ListAPIView):
    queryset = WorkoutProgram.objects.filter(is_public=True)
    serializer_class = WorkoutProgramSerializer

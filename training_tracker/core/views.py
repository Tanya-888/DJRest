from rest_framework import viewsets
from .models import (
    User,
    CoachProfile,
    WorkoutProgram,
    Exercise,
    UserWorkoutPlan,
    ExerciseResult,
    Reminder
)
from .serializers import (
    UserSerializer,
    CoachProfileSerializer,
    WorkoutProgramSerializer,
    ExerciseSerializer,
    UserWorkoutPlanSerializer,
    ExerciseResultSerializer,
    ReminderSerializer
)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CoachProfileViewSet(viewsets.ModelViewSet):
    queryset = CoachProfile.objects.all()
    serializer_class = CoachProfileSerializer

class WorkoutProgramViewSet(viewsets.ModelViewSet):
    queryset = WorkoutProgram.objects.all()
    serializer_class = WorkoutProgramSerializer

class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

class UserWorkoutPlanViewSet(viewsets.ModelViewSet):
    queryset = UserWorkoutPlan.objects.all()
    serializer_class = UserWorkoutPlanSerializer

class ExerciseResultViewSet(viewsets.ModelViewSet):
    queryset = ExerciseResult.objects.all()
    serializer_class = ExerciseResultSerializer

class ReminderViewSet(viewsets.ModelViewSet):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
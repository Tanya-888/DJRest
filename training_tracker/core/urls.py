from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserViewSet,
    CoachProfileViewSet,
    WorkoutProgramViewSet,
    ExerciseViewSet,
    UserWorkoutPlanViewSet,
    ExerciseResultViewSet,
    ReminderViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'coach-profiles', CoachProfileViewSet)
router.register(r'workout-programs', WorkoutProgramViewSet)
router.register(r'exercises', ExerciseViewSet)
router.register(r'user-workout-plans', UserWorkoutPlanViewSet)
router.register(r'exercise-results', ExerciseResultViewSet)
router.register(r'reminders', ReminderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

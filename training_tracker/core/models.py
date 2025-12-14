from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('guest', 'Гость'),
        ('member', 'Пользователь'),
        ('trainer', 'Тренер'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='guest')


class CoachProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)


class WorkoutProgram(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={'role': 'trainer'}
    )
    is_public = models.BooleanField(default=False)


class Exercise(models.Model):
    program = models.ForeignKey(WorkoutProgram, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    reps = models.IntegerField()
    sets = models.IntegerField()


class UserWorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='workout_plans')
    program = models.ForeignKey(WorkoutProgram, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    completed = models.BooleanField(default=False)


class ExerciseResult(models.Model):
    user_plan = models.ForeignKey(UserWorkoutPlan, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    date = models.DateField()
    achieved_reps = models.IntegerField()
    notes = models.TextField(blank=True)


class Reminder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    scheduled_time = models.DateTimeField()
    message = models.CharField(max_length=255)

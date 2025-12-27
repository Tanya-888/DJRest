
# Register your models here.

from django.contrib import admin
from .models import User, CoachProfile, WorkoutProgram, Exercise, UserWorkoutPlan, ExerciseResult, Reminder

admin.site.register(User)
admin.site.register(CoachProfile)
admin.site.register(WorkoutProgram)
admin.site.register(Exercise)
admin.site.register(UserWorkoutPlan)
admin.site.register(ExerciseResult)
admin.site.register(Reminder)
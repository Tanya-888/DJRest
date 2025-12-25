from django import forms
from .models import WorkoutProgram, Exercise, UserWorkoutPlan, ExerciseResult

class WorkoutProgramForm(forms.ModelForm):
    class Meta:
        model = WorkoutProgram
        fields = ['title', 'description', 'is_public']

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['program', 'name', 'description', 'reps', 'sets']

class UserWorkoutPlanForm(forms.ModelForm):
    class Meta:
        model = UserWorkoutPlan
        fields = ['user', 'program', 'start_date', 'end_date', 'completed']

class ExerciseResultForm(forms.ModelForm):
    class Meta:
        model = ExerciseResult
        fields = ['user_plan', 'exercise', 'date', 'achieved_reps', 'notes']
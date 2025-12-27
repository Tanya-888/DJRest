from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import CoachProfile, WorkoutProgram, Exercise, UserWorkoutPlan, ExerciseResult, Reminder

User = get_user_model()

class ModelTests(TestCase):

    def setUp(self):
        # пользователь
        self.user = User.objects.create_user(username='testuser', password='testpassword', role='trainer')

    def test_create_user(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.role, 'trainer')

    def test_coach_profile_creation(self):
        profile = CoachProfile.objects.create(user=self.user, bio='Эксперт по тренировкам')
        self.assertEqual(profile.user, self.user)
        self.assertEqual(profile.bio, 'Эксперт по тренировкам')

    def test_workout_program(self):
        program = WorkoutProgram.objects.create(
            title='Программа 1',
            description='Описание программы',
            created_by=self.user,
            is_public=True
        )
        self.assertEqual(program.title, 'Программа 1')
        self.assertEqual(program.created_by, self.user)
        self.assertTrue(program.is_public)

    def test_exercise(self):
        program = WorkoutProgram.objects.create(title='Test Prog', created_by=self.user)
        exercise = Exercise.objects.create(
            program=program,
            name='Push-up',
            description='Отжимания',
            reps=10,
            sets=3
        )
        self.assertEqual(exercise.name, 'Push-up')
        self.assertEqual(exercise.reps, 10)

    def test_user_workout_plan(self):
        program = WorkoutProgram.objects.create(title='Prog', created_by=self.user)
        plan = UserWorkoutPlan.objects.create(
            user=self.user,
            program=program,
            start_date='2024-01-01',
            end_date='2024-01-07',
            completed=False
        )
        self.assertEqual(plan.user, self.user)
        self.assertFalse(plan.completed)

    def test_exercise_result(self):
        program = WorkoutProgram.objects.create(title='Prog', created_by=self.user)
        plan = UserWorkoutPlan.objects.create(
            user=self.user,
            program=program,
            start_date='2024-01-01',
            end_date='2024-01-07'
        )
        exercise = Exercise.objects.create(
            program=program,
            name='Squat',
            reps=15,
            sets=4
        )
        result = ExerciseResult.objects.create(
            user_plan=plan,
            exercise=exercise,
            date='2024-01-02',
            achieved_reps=15,
            notes='Good'
        )
        self.assertEqual(result.achieved_reps, 15)

    def test_reminder(self):
        exercise = Exercise.objects.create(
            program=WorkoutProgram.objects.create(title='Prog', created_by=self.user),
            name='Jumping Jack',
            reps=20,
            sets=3
        )
        reminder = Reminder.objects.create(
            user=self.user,
            exercise=exercise,
            scheduled_time='2024-01-01T10:00:00',
            message='Напоминание о тренировке'
        )
        self.assertEqual(reminder.message, 'Напоминание о тренировке')

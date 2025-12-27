from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.utils import timezone
from .models import (
    User, CoachProfile, WorkoutProgram, Exercise,
    UserWorkoutPlan, ExerciseResult, Reminder
)

class YourAppTests(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.user = User.objects.create_user(username='testuser', password='password')

        self.coach_profile = CoachProfile.objects.create(user=self.user, bio='Test bio')

        self.workout_program = WorkoutProgram.objects.create(title='Test Program')

        self.exercise = Exercise.objects.create(
            program=self.workout_program,
            name='Push-up',
            description='Upper body exercise',
            reps=10,
            sets=3
        )

        #  план тренировок
        self.user_workout_plan = UserWorkoutPlan.objects.create(
            user=self.user,
            program=self.workout_program,
            start_date='2024-01-01',
            end_date='2024-01-07'
        )

        #  результат выполнения упражнения
        self.exercise_result = ExerciseResult.objects.create(
            user_plan=self.user_workout_plan,
            exercise=self.exercise,
            date='2024-01-01',
            achieved_reps=10,
            notes='Good'
        )

        # напоминание
        self.reminder = Reminder.objects.create(
            user=self.user,
            exercise=self.exercise,
            scheduled_time=timezone.now(),
            message='Drink water'
        )


    def test_list_users(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)

    def test_create_user(self):
        url = reverse('user-list')
        data = {'username': 'newuser', 'password': 'password123'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['username'], 'newuser')

    def test_retrieve_user(self):
        url = reverse('user-detail', args=[self.user.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], self.user.username)

    def test_update_user(self):
        url = reverse('user-detail', args=[self.user.id])
        data = {'username': 'updateduser'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')

    def test_delete_user(self):
        url = reverse('user-detail', args=[self.user.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(User.objects.filter(id=self.user.id).exists())
from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create(name="Test User", email="test@example.com", team="marvel")
        self.assertEqual(user.name, "Test User")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.team, "marvel")

class TeamModelTest(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name="marvel", members=["Test User"])
        self.assertEqual(team.name, "marvel")
        self.assertIn("Test User", team.members)

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        activity = Activity.objects.create(user="Test User", activity="Running", duration=10)
        self.assertEqual(activity.user, "Test User")
        self.assertEqual(activity.activity, "Running")
        self.assertEqual(activity.duration, 10)

class LeaderboardModelTest(TestCase):
    def test_create_leaderboard(self):
        lb = Leaderboard.objects.create(team="marvel", points=50)
        self.assertEqual(lb.team, "marvel")
        self.assertEqual(lb.points, 50)

class WorkoutModelTest(TestCase):
    def test_create_workout(self):
        workout = Workout.objects.create(name="Push Ups", difficulty="Easy")
        self.assertEqual(workout.name, "Push Ups")
        self.assertEqual(workout.difficulty, "Easy")

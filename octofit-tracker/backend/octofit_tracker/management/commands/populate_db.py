from django.core.management.base import BaseCommand
from django.conf import settings
from pymongo import MongoClient, ASCENDING

# サンプルデータ
USERS = [
    {"name": "Iron Man", "email": "ironman@marvel.com", "team": "marvel"},
    {"name": "Captain America", "email": "cap@marvel.com", "team": "marvel"},
    {"name": "Spider-Man", "email": "spiderman@marvel.com", "team": "marvel"},
    {"name": "Superman", "email": "superman@dc.com", "team": "dc"},
    {"name": "Batman", "email": "batman@dc.com", "team": "dc"},
    {"name": "Wonder Woman", "email": "wonderwoman@dc.com", "team": "dc"},
]
TEAMS = [
    {"name": "marvel", "members": ["Iron Man", "Captain America", "Spider-Man"]},
    {"name": "dc", "members": ["Superman", "Batman", "Wonder Woman"]},
]
ACTIVITIES = [
    {"user": "Iron Man", "activity": "Running", "duration": 30},
    {"user": "Superman", "activity": "Flying", "duration": 60},
]
LEADERBOARD = [
    {"team": "marvel", "points": 100},
    {"team": "dc", "points": 120},
]
WORKOUTS = [
    {"name": "Push Ups", "difficulty": "Easy"},
    {"name": "Squats", "difficulty": "Medium"},
]

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        client = MongoClient(host='localhost', port=27017)
        db = client['octofit_db']

        # コレクションの初期化
        db.users.delete_many({})
        db.teams.delete_many({})
        db.activities.delete_many({})
        db.leaderboard.delete_many({})
        db.workouts.delete_many({})

        # データ挿入
        db.users.insert_many(USERS)
        db.teams.insert_many(TEAMS)
        db.activities.insert_many(ACTIVITIES)
        db.leaderboard.insert_many(LEADERBOARD)
        db.workouts.insert_many(WORKOUTS)

        # emailフィールドにユニークインデックス
        db.users.create_index([("email", ASCENDING)], unique=True)

        self.stdout.write(self.style.SUCCESS('octofit_dbにテストデータを投入しました'))

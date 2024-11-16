# models.py
from django.db import models
from django.contrib.auth.models import User

class TypingContest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    contest_id = models.IntegerField()  # Identify the contest
    wpm = models.FloatField()  # Words Per Minute
    accuracy = models.FloatField()  # Accuracy percentage
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - WPM: {self.wpm}, Accuracy: {self.accuracy}"
    

class TypingContext(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)


class Score(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    wpm = models.FloatField()
    accuracy = models.FloatField()
    # other fields as necessary

#user data saving
from django.db import models
from django.contrib.auth.models import User

class TypingData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    speed = models.FloatField()
    accuracy = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

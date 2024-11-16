# admin.py
from django.contrib import admin
from .models import TypingContest

@admin.register(TypingContest)
class TypingContestAdmin(admin.ModelAdmin):
    list_display = ("user", "contest_id", "wpm", "accuracy", "timestamp")

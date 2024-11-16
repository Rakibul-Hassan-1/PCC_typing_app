from django import forms
from .models import TypingContext
from django.utils import timezone
from datetime import datetime

class TypingContextForm(forms.ModelForm):
    start_time = forms.DateTimeField(widget=forms.HiddenInput(), initial=datetime.now)

    class Meta:
        model = TypingContext
        fields = ['text', 'start_time']


class TypingTestForm(forms.Form):
    text_entered = forms.CharField(widget=forms.Textarea, label="Type here")
    start_time = forms.DateTimeField(widget=forms.HiddenInput())

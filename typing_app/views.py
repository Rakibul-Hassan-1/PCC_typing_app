from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TypingContextForm  
from .forms import TypingContextForm
from django.utils import timezone
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# logout 
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('home')

# dashboard
@login_required
def dashboard(request):
    return render(request, 'typing_app/dashboard.html')

# contest
from django.shortcuts import render
def typing_contest(request):
    return render(request, 'typing_app/contest.html')  # Render the provided HTML

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def calculate_score(submitted_text, start_time, end_time):
    """
    Calculate score based on characters per minute.
    - submitted_text: the text input by the user
    - start_time: datetime when typing started
    - end_time: datetime when typing ended
    """
    duration = (end_time - start_time).total_seconds() / 60  # Convert time to minutes
    char_count = len(submitted_text)
    if duration > 0:
        cpm = char_count / duration  # characters per minute
    else:
        cpm = 0
    return int(cpm)

def submit_typing_context(request):
    if request.method == 'POST':
        form = TypingContextForm(request.POST)
        if form.is_valid():
            typing_context = form.save(commit=False)
            typing_context.user = request.user
            # Assuming you collect start and end times via the form or JavaScript in the template
            start_time = form.cleaned_data['start_time']
            end_time = timezone.now()  # Capture end time when the form is submitted
            typing_context.score = calculate_score(form.cleaned_data['text'], start_time, end_time)
            typing_context.save()
            return redirect('leaderboard')  # Redirect to the leaderboard view
    else:
        form = TypingContextForm()
    return render(request, 'submit_context.html', {'form': form})


def contest_view(request):
    leaderboard = [
        {'user_name': 'John Doe', 'wpm': 90, 'position': '1st', 'position_class': 'first-place', 'badge_class': 'badge-success'},
        {'user_name': 'Jane Smith', 'wpm': 85, 'position': '2nd', 'position_class': 'second-place', 'badge_class': 'badge-warning'},
        {'user_name': 'Michael Brown', 'wpm': 80, 'position': '3rd', 'position_class': 'third-place', 'badge_class': 'badge-danger'},
        # More participants
    ]
    return render(request, 'contest.html', {'leaderboard': leaderboard})


from .models import Score 
def leaderboard_view(request):
    leaderboard_scores = Score.objects.all().order_by('-wpm')[:10]  # Adjust the query as needed
    return render(request, 'leaderboard.html', {'leaderboard': leaderboard_scores})

# testing korlam
# def leaderboard_view(request):
#     print("View is called")
#     leaderboard = [
#         {'user': {'username': 'testuser1'}, 'wpm': 80, 'accuracy': 98},
#         {'user': {'username': 'testuser2'}, 'wpm': 75, 'accuracy': 96},
#     ]
#     print(leaderboard)
#     return render(request, 'leaderboard.html', {'leaderboard': leaderboard})

# your_app/views.py
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.http import HttpResponse

def some_view(request):
    # your view logic here
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        "leaderboard_group",
        {
            "type": "send_leaderboard_data",
            "data": {
                "leaderboard": "new leaderboard data"
            }
        }
    )
    return HttpResponse("Leaderboard updated")

#user data saving
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import pandas as pd
from .models import TypingData

@login_required
def save_to_excel(request):
    user_data = TypingData.objects.filter(user=request.user).values(
        'speed', 'accuracy', 'timestamp'
    )

    # print(list(user_data))  # Add this line for debugging

    if user_data.exists():
        df = pd.DataFrame(list(user_data))
        df.rename(columns={
            'speed': 'Typing Speed (WPM)',
            'accuracy': 'Accuracy (%)',
            'timestamp': 'Test Date & Time'
        }, inplace=True)
    else:
        df = pd.DataFrame(columns=['Typing Speed (WPM)', 'Accuracy (%)', 'Test Date & Time'])

    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = f'attachment; filename="{request.user.username}_typing_data.xlsx"'
    df.to_excel(response, index=False)
    return response


from .models import TypingData

def save_typing_data(request, speed, accuracy):
    if request.user.is_authenticated:
        TypingData.objects.create(
            user=request.user,
            speed=speed,
            accuracy=accuracy
        )

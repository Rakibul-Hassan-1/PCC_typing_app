from django.urls import path
from django.urls import path
from .views import leaderboard_view
from . import views
from .views import save_to_excel
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('contest/', views.typing_contest, name='typing_contest'),
    path('leaderboard/', leaderboard_view, name='leaderboard'),
    path('save-excel/', views.save_to_excel, name='save_to_excel'),


]

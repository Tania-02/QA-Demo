from django.urls import path
from  .views import *

urlpatterns = [
    path('', index, name="index"),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('question/<int:question_id>', question, name='question'),
    path('leaderboard/', leaderboard, name='leaderboard'),
]

"""Routes for application"""
from django.urls import path
from api.views import (GameView,GameDeveloperView)

app_name = "api"

urlpatterns = [
    path('games/',GameView.as_view(),name="game"),
    path('games/<int:game_id>/',GameView.as_view(),name="game_with_id"),
    path('game/developer/',GameDeveloperView.as_view(),name="game_developer"),
    path('game/developer/<int:game_developer_id>',GameDeveloperView.as_view(),name="game_developer_with_id")
]

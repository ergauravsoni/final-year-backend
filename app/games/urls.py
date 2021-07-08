from django.urls import path

from . import views

app_name = 'games'

urlpatterns = [
    path('score_list/', views.ListGameScoreView.as_view(), name='score_list'),
    path('score_create/', views.CreateGameScoreView.as_view(), name='score_create'),
    path('score_update/', views.ManageGameScoreView.as_view(), name='score_update'),
]

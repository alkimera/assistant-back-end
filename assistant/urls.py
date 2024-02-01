from django.urls import path
from .views import UserSpeechView

urlpatterns = [
    path('user-speech/', UserSpeechView.as_view(), name='user_speech'),
]

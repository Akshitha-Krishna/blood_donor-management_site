
from django.urls import path
from .views import FindMatchView

urlpatterns = [
    path('find/',FindMatchView.as_view()),
]
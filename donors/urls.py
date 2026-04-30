
from django.urls import path
from .views import DonorMeView,ToggleAvailabilityView

urlpatterns = [
    path('me/',DonorMeView.as_view()),
    path('availability/',ToggleAvailabilityView.as_view())
]
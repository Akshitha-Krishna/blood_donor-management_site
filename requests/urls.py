
from django.urls import path
from .views import RequestListCreateView,RequestDetailView

urlpatterns = [
    path('requests/',RequestListCreateView.as_view()),
    path('details/',RequestDetailView.as_view()),
    
]
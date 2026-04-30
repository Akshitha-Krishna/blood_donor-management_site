from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import BloodRequest
from .serializers import requestSerializer

# Create your views here.
class RequestListCreateView(ListCreateAPIView):
    queryset = BloodRequest.objects.all()
    serializer_class = requestSerializer

class RequestDetailView(RetrieveUpdateDestroyAPIView):
    queryset = BloodRequest.objects.all()
    serializer_class = requestSerializer
    

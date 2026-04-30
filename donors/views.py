from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import DonorProfile

# Create your views here.
class DonorMeView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        donor = DonorProfile.objects.get(user=request.user)
        data = {
            "blood_group":donor.blood_group,
            "location":donor.location,
            "available":donor.available
        }
        return Response(data)

# PUT /api/donor/me
    def put(self,request):
        donor = DonorProfile.objects.get(user=request.user)
        serializer = DonorSerializer(donor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.error,status=400)

# GET / api/donors/availabilty
class ToggleAvailabilityView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self,request):
        donor = DonorProfile.objects.get(user=request.user)
        donor.available = not donor.available
        donor.save()
        return Response({"available":donor.available})

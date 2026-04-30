from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .services import find_matching_donors
from .serializers import MatchSerializer

# Create your views here.
class FindMatchView(APIView):
    def post(self,request):
        blood_group=request.data.get("blood_group")
        donors = find_matching_donors(blood_group)

        data = [
            {
            "id": d.id,
            "blood_group": d.blood_group,
            "location": d.location
            }
            for d in donors
        ]
        return Response(data)

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer
'''
from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()
'''
class RegisterView(APIView):
    def post(self,request):
        print("hello")
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)





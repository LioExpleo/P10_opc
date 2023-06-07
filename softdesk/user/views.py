from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView # pour APIView
from rest_framework.response import Response # pour APIView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.decorators import api_view
from rest_framework import status
#@api_view(['POST'])

class GetRegisterView(APIView):
    def get(self, *args, **kwargs):
        queryset = User.objects.all()

        serializer = RegisterSerializer(queryset, many=True)  # many permet de sérialiser plusieurs catégories si besoin
        return Response(serializer.data)

class PostRegisterView(APIView):
    def post(self, *args, **kwargs):
        queryset = User.objects.all()

        serializer = RegisterSerializer(queryset, many=True)  # many permet de sérialiser plusieurs catégories si besoin
        return Response(serializer.data)


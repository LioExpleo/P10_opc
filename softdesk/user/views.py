from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView # pour APIView
from rest_framework.response import Response # pour APIView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.decorators import api_view
from rest_framework import status
#@api_view(['POST'])
from django.views.decorators.http import require_http_methods

class GetRegisterView(APIView):
    def get(self, *args, **kwargs):
        queryset = User.objects.all()

        serializer = RegisterSerializer(queryset, many=True)  # many permet de sérialiser plusieurs catégories si besoin
        return Response(serializer.data)

# @api_view(['POST'])
class PostRegisterView(APIView):
    # @require_http_methods(["GET"])
    def get(self, *args, **kwargs):
        queryset = User.objects.all()

        serializer = RegisterSerializer(queryset, many=True)  # many permet de sérialiser plusieurs catégories si besoin
        return Response(serializer.data)

    # @require_http_methods(["POST"])
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response ({'Error': 'data invalides'})



from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView # pour APIView
from rest_framework.response import Response # pour APIView
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.decorators import api_view
from rest_framework import status
#@api_view(['POST'])
from django.views.decorators.http import require_http_methods

from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class GetRegisterView(APIView):
    def get(self, *args, **kwargs):
        queryset = User.objects.all()

        serializer = RegisterSerializer(queryset, many=True)  # many permet de sérialiser plusieurs catégories si besoin
        return Response(serializer.data)

# @api_view(['POST'])
class RegisterView(APIView):
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
            return Response("Pas de création de cet utilisateur", serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from django.contrib.auth import authenticate, login
class LoginView0(APIView):
    def post(request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return Response("Utilisateur connecté")
            # Redirect to a success page.
            ...
        else:
            return Response("Pas de création de cet utilisateur")
            # Return an 'invalid login' error message.
            ...

    def get(self, *args, **kwargs):
        queryset = User.objects.all()

        serializer = RegisterSerializer(queryset, many=True)  # many permet de sérialiser plusieurs catégories si besoin
        return Response(serializer.data)
class LoginView(APIView):

    # @require_http_methods(["POST"])
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        return Response(serializer.data)

class LoginView2(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        content = {
            'user': str(request.user),  # `django.contrib.auth.User` instance.
            'auth': str(request.auth),  # None
        }
        return Response(content)


'''
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
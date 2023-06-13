from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView  # pour APIView
from rest_framework.response import Response  # pour APIView

from .models import Person, ModelTest, Projects, User
from .serializers import PersonSerializer, TestSerializer, ProjectSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import status

class PersonView(APIView):
    def get(self, *args, **kwargs):
        queryset = Person.objects.all()
        serializer = PersonSerializer(queryset, many=True)  # many permet de sérialiser plusieurs catégories si besoin
        return Response(serializer.data)

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):

            serializer.save()
            return Response(serializer.data)
        else:
            return Response({'Error': 'data invalides'})


class TestViewset(ReadOnlyModelViewSet):
    serializer_class = TestSerializer

    def get_queryset(self):
        queryset = ModelTest.objects.filter(active=True)
        test_id = self.request.GET.get('test_id')  # verifie si test_id est dans l'url
        if test_id is not None:  # si test_id est dans l'url, filtrer avec test_id de l'url = id
            queryset = queryset.filter(id=test_id)
        else:
            pass
        return queryset


'''
        serializer = TestSerializer(queryset, many=True)  # many permet de sérialiser plusieurs catégories si besoin
        return ModelTest.objects.filter(active=True)
'''


class ProjectsView(APIView):
    auth_user_id = User.pk  # mettre l'utilisateur connecté du projet
    def get(self, *args, **kwargs):
        queryset = Projects.objects.all()
        serializer = ProjectSerializer(queryset, many=True)  # many permet de sérialiser plusieurs catégories si besoin
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

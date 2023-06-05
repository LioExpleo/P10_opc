from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView # pour APIView
from rest_framework.response import Response # pour APIView

from .models import Person, ModelTest
from .serializers import PersonSerializer, TestSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet

class PersonView(APIView):
    def get(self, *args, **kwargs):
        queryset = Person.objects.all()
        serializer = PersonSerializer(queryset, many=True)  # many permet de sérialiser plusieurs catégories si besoin
        return Response(serializer.data)
'''
class TestView(APIView):
    def get(self, *args, **kwargs):
        queryset = ModelTest.objects.all()
        serializer = TestSerializer(queryset, many=True)  # many permet de sérialiser plusieurs catégories si besoin
        return Response(serializer.data)
'''
class TestViewset(ReadOnlyModelViewSet):
    serializer_class = TestSerializer
    def get_queryset(self):
        queryset = ModelTest.objects.all()
        serializer = TestSerializer(queryset, many=True)  # many permet de sérialiser plusieurs catégories si besoin
        return ModelTest.objects.all()
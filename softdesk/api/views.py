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

'''
class TestViewset(ReadOnlyModelViewSet):
    serializer_class = TestSerializer
    def get_queryset(self):
        queryset = ModelTest.objects.all()
        serializer = TestSerializer(queryset, many=True)  # many permet de sérialiser plusieurs catégories si besoin
        return ModelTest.objects.filter(active=True)
'''

class TestViewset(ReadOnlyModelViewSet):
    serializer_class = TestSerializer
    def get_queryset(self):
        queryset = ModelTest.objects.filter(active=True)
        test_id = self.request.GET.get('test_id') # verifie si test_id est dans l'url
        if test_id is not None: # si test_id est dans l'url, filtrer avec test_id de l'url = id
            queryset = queryset.filter(id=test_id)
        else:
            pass
        return queryset


'''
        serializer = TestSerializer(queryset, many=True)  # many permet de sérialiser plusieurs catégories si besoin
        return ModelTest.objects.filter(active=True)
'''

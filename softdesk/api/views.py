from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView  # pour APIView
from rest_framework.response import Response  # pour APIView

from .models import Person, ModelTest, Projects, User
from .serializers import PersonSerializer, TestSerializer, ProjectSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import status, filters, request

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

class ProjectsViewset(ReadOnlyModelViewSet): # class ProjectsView(APIView):
    # auth_user_id = User.pk  # mettre l'utilisateur connecté du projet
    serializer_class = ProjectSerializer


    def get_queryset(self):                             #def get(self, *args, **kwargs):
        queryset = Projects.objects.all()
        #serializer = ProjectSerializer(queryset, many=True)  # many permet de sérialiser plusieurs catégories si besoin

        project_id = self.request.GET.get('project_id')
        queryset = Projects.objects.all() # recupérer tous les projets
        # si id is not None, on filtre avec l'id correspondant au projet et on renvoie le résultat

        #if project_id is not None:
        #    pass
            #queryset = Projects.objects.all()
            #queryset = queryset.filter(project_id=project_id)
            #return queryset    # return Response(serializer.data)
        # sinon, on renvoie tout les objets
        #else: # si pas d'id
        return queryset

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #def put(self, request, pk): #mettre *args, **kwargs au lieu de pk évite le plantage si pk absent.
    def put(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        try :
            projet = Projects.objects.get(pk=pk)
        except:
            projet = "pas de projet"
        #project_id = self.request.GET.get('project_id')
        serializer = ProjectSerializer(data=request.data)
        queryset = Projects.objects.all()  # recupérer tous les projets

        if projet != "pas de projet":
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        else:
            return Response("pas de projet sélectionné existant ***, http://127.0.0.1:8000/projects/***")

    def delete(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        try :
            projet = Projects.objects.get(pk=pk)
        except:
            projet = "pas de projet"
            pass
        serializer = ProjectSerializer(data=request.data)

        if projet != "pas de projet":
            projet.delete()
            return Response("projet supprimé avec succès", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("pas de projet sélectionné existant ***, http://127.0.0.1:8000/projects/***")

class ProjectsIdViewset(ReadOnlyModelViewSet): # class ProjectsView(APIView):
    # auth_user_id = User.pk  # mettre l'utilisateur connecté du projet
    serializer_class = ProjectSerializer
    def get_queryset(self):                             #def get(self, *args, **kwargs):
        # queryset = Projects.objects.all()
        #serializer = ProjectSerializer(queryset, many=True)  # many permet de sérialiser plusieurs catégories si besoin
        project_id = self.request.GET.get('project_id')
        queryset = Projects.objects.all() # recupérer tous les projets
        # si id is not None, on filtre avec l'id correspondant au projet et on renvoie le résultat
        if project_id is not None:
            queryset = queryset.filter(project_id=project_id)
            return queryset    # return Response(serializer.data)
        # sinon, on renvoie tout les objets
        else:
            return queryset

    def put(self, request, pk):
        project_id = self.request.GET.get('project_id')
        serializer = ProjectSerializer(data=request.data)
        queryset = Projects.objects.all()  # recupérer tous les projets
        #if project_id is not None:
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        project_id = self.request.GET.get('project_id')
        serializer = ProjectSerializer(data=request.data)
        #project = self.get_object(pk)
        #self.check_object_permissions(request, obj=project)
        #project.delete()
        #return Response(status=status.HTTP_204_NO_CONTENT)
        queryset = Projects.objects.all()

        #if serializer.is_valid(raise_exception=True):

        if project_id is not None:
            queryset = queryset.filter(project_id=project_id)
            project_id.delete(project_id)
            #return Response(serializer.data, status=status.HTTP_201_CREATED)  # return Response(serializer.data)
        # sinon, on renvoie tout les objets
        else:
            pass
                #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


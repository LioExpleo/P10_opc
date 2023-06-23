from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView  # pour APIView
from rest_framework.response import Response  # pour APIView

from .models import Person, ModelTest, Projects, User, Contributor, Issue, Comment
from .serializers import PersonSerializer, TestSerializer, ProjectSerializer, ContributorSerializer, IssueSerializer, CommentSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import status, filters, request
from django.shortcuts import get_object_or_404

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

    def post(self, request, *args, **kwargs):

        pk = self.kwargs.get('pk')
        try :
            projet = Projects.objects.get(pk=pk)
        except:
            projet = "pas de projet"

        if projet == "pas de projet": # si pas de projet sélectionné, post possible, voir si utile
            serializer = ProjectSerializer(data=request.data)

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else: # si un projet sélectionné, post possible, voir si utile
            serializer = ProjectSerializer(data=request.data)

            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            #return Response("Ne pas sélectionner de projet pour en créer un nouveau, http://127.0.0.1:8000/projects/ (ID)")

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
            return Response("pas de projet sélectionné existant dans le navigateur pour update***, http://127.0.0.1:8000/projects/ (ID)")

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

class ContributorsView(APIView): # class ProjectsView(APIView):
    serializer_class = ContributorSerializer

    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        try:
            projet = Projects.objects.get(pk=pk)
        except:
            projet = "pas de projet"

        contributors = Contributor.objects.filter(project_id=pk)
        serializer = ContributorSerializer(contributors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):

        serializer = ContributorSerializer(data=self.request.data)
        pk = self.kwargs.get('pk')
        try:
            proj = Contributor.objects.get(pk=pk)
        except:
            proj = "pas de projet"

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContributorsDelView(APIView):  # class ProjectsView(APIView):
    serializer_class = ContributorSerializer
    def get(self, request, *args, **kwargs):
        pk_project = self.kwargs.get('pk')
        pk_contrib = self.kwargs.get('pk_contrib')

        contributor_projet = Contributor.objects.filter(project_id=pk_project, user_id=pk_contrib)
        #contributors = Contributor.objects.filter( user_id=pk2)
        serializer = ContributorSerializer(contributor_projet, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        pk_project = self.kwargs.get('pk')
        pk_contrib = self.kwargs.get('pk_contrib')

        contributor_projet = Contributor.objects.filter(project_id=pk_project, user_id=pk_contrib)
        # contributors = Contributor.objects.filter( user_id=pk2)
        serializer = ContributorSerializer(contributor_projet, many=True)
        contributor_projet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) #requete réussie, mais pas besoin de quitter la page

class IssueView(APIView):  # class ProjectsView(APIView):
    serializer_class = IssueSerializer
    def get(self, request, *args, **kwargs):
        pk_project = self.kwargs.get('pk')
        #pk_issue = self.kwargs.get('pk_issue')

        issue_projet = Issue.objects.filter(project_id=pk_project)
        # issue_projet = Issue.objects.filter(project_id=pk_project, user_id=pk_issue)

        serializer = IssueSerializer(issue_projet, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) #requete réussie, mais pas besoin de quitter la page

    def post(self, request, *args, **kwargs):

        serializer = IssueSerializer(data=self.request.data)
        pk = self.kwargs.get('pk')
        try:
            proj = Contributor.objects.get(pk=pk)
        except:
            proj = "pas de projet"

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IssuePutView(APIView):  # class ProjectsView(APIView):
    serializer_class = IssueSerializer

    def get(self, request, *args, **kwargs):
        pk_project = self.kwargs.get('pk')
        pk_issue = self.kwargs.get('pk_issue')

        #issue_projet = Issue.objects.filter(project_id=pk_project, id=pk_issue)
        issue_projet = Issue.objects.filter(project_id=pk_project, id=pk_issue)
        # contributors = Contributor.objects.filter( user_id=pk2)
        serializer = IssueSerializer(issue_projet, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        pk_issue = self.kwargs.get('pk_issue')

        try:
            projet = Projects.objects.get(pk=pk)
        except:
            projet = "pas de projet"
            return Response(
                "pas de projet sélectionné existant dans le navigateur pour update***, http://127.0.0.1:8000/projects/ "
                "pour visualiser les projets existants")
        serializer = IssueSerializer(data=request.data)
        #queryset = Projects.objects.all()  # recupérer tous les projets

        if projet != "pas de projet":
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        else:
            return Response(
                "pas de projet sélectionné existant dans le navigateur pour update***, http://127.0.0.1:8000/projects/ "
                "pour visualiser les projets existants")

    def delete(self, request, *args, **kwargs):
        pk_project = self.kwargs.get('pk')
        pk_issue = self.kwargs.get('pk_issue')

        issue_projet = Issue.objects.filter(project_id=pk_project, id=pk_issue)
        serializer = IssueSerializer(issue_projet, many=True)

        issue_projet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  # requete réussie, mais pas besoin de quitter la page



class CommentView(APIView):  # class ProjectsView(APIView):
    serializer_class = CommentSerializer

    def get(self, request, *args, **kwargs):
        pk_project = self.kwargs.get('pk') # recup id projet
        pk_issue = self.kwargs.get('pk_issue') # recup id issue
        filtre_comments = Comment.objects.filter(issue_id=pk_issue) # recup comment ayant id issue dans le navigateur
        serializer = CommentSerializer(filtre_comments, many=True) # serializer comment ayant id issue
        #pk_comment = self.kwargs.get('pk_comment')
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=self.request.data)
        pk_issue = self.kwargs.get('pk_issue')  # recup id issue
        #filtre_comments = Comment.objects.filter(issue_id=pk_issue)  # recup comment ayant id issue dans le navigateur
        #serializer = CommentSerializer(filtre_comments, many=True)  # serializer comment ayant id issue

        try:
            comment = Comment.objects.get(pk_issue=pk_issue)
        except:
            comment = "pas de projet"

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


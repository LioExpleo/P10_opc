from rest_framework.serializers import ModelSerializer
from .models import Person, ModelTest, Projects, User, TYPE_CHOICES
from rest_framework import serializers, request
from rest_framework.validators import UniqueValidator

class PersonSerializer(ModelSerializer):
     class Meta:
            model = Person
            #fields = ['modele1_name', 'modele1_last_name']
            fields = "__all__" # utiliser tous les champs du modèle


class TestSerializer(ModelSerializer):
    class Meta:
        model = ModelTest
        fields = "__all__"  # utiliser tous les champs du modèle
        #fields = ['id', ' Test_FirstName', 'Test_LastName']

class ProjectSerializer(ModelSerializer):
    title = serializers.CharField(required=True, validators=[UniqueValidator(queryset=Projects.objects.all())])
    description = serializers.CharField(required=True)
    type = serializers.CharField(required=True)

    class Meta:
        model = Projects
        fields = "__all__"
from rest_framework.serializers import ModelSerializer
from .models import Person, ModelTest

class PersonSerializer(ModelSerializer):
     class Meta:
            model = Person
            #fields = ['modele1_name', 'modele1_last_name']
            fields = "__all__" # utiliser tous les champs du modèle


class TestSerializer(ModelSerializer):
    class Meta:
        model = ModelTest
        # fields = ['modele1_name', 'modele1_last_name']
        fields = "__all__"  # utiliser tous les champs du modèle
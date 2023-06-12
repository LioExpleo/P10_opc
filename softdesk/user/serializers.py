from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
#from models import

class RegisterSerializer(ModelSerializer):
    # Les champs ci-dessous sont requis, et uniques.
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    first_name = serializers.CharField(required=True, validators= [UniqueValidator(queryset=User.objects.all())])
    last_name = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])

    # Même si la requête a is-staff et is_superuser à true, ça n'est pas pris en compte dans la base de donnée

    class Meta:
        model = User
        #fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        fields = "__all__"  # utiliser tous les champs du modèle


    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        user.set_password(validated_data['password']) # validation password par django, password non codé dans bdd si absent.
        user.save()
        return user

class LoginSerializer(ModelSerializer):
    class Meta:
        model = login
        fields = "__all__"


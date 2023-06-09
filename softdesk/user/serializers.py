from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

#from models import

class RegisterSerializer(ModelSerializer):
    # username = serializers.CharField
    # email = serializers.EmailField
    class Meta:
        model = User

        #fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        # fields = ['modele1_name', 'modele1_last_name']
        fields = "__all__"  # utiliser tous les champs du modèle


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')

class LoginSerializer(ModelSerializer):
    class Meta:
        model = login
        fields = "__all__"






# No backend authenticated the credentials

'''
    def create(self, validated_data):
        user = User.objects.create(
            username=['username'],
            email=['email'],
            first_name=['first_name'],
            last_name=['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
'''
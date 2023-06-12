from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
#from models import

class RegisterSerializer(ModelSerializer):
    # Les champs username et email du serializer sont requis, et uniques.
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

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
'''
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email')
        # fields = "__all__"
'''
class LoginSerializer(ModelSerializer):
    class Meta:
        model = login
        fields = "__all__"

class SignupSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"




class RegisterSerializerCreat(serializers.ModelSerializer):
    '''
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    '''
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email', 'first_name', 'last_name')
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True},
            # 'username': {'unique': True},
            # 'email': {'unique': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user



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

class RegisterSerializer2(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
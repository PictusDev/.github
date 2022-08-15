from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate

from .models import Profile

class RegisterSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password=serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )

    class Meta:
        model=User
        fields=['id','username', 'password','email']
    
    def create(self, validated_data):
        user =User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()
        token=Token.objects.create(user=user)
        return user



class LoginSerializer(serializers.Serializer):
    email=serializers.CharField(required=True)
    password=serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        email=data.get("email",None)
        password=data.get("password",None)

        if User.objects.filter(email=email).exists():
            user=User.objects.get(email=email)

            if not user.check_password(password):
                raise serializers.ValidationError()
            else:
                return user

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=["url","information","image"]

    
class ProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields=["user","nickname","url","information","image","email"]



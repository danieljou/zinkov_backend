from rest_framework import serializers
# from django.contrib.auth.models import User

from .models import *

class   UserSeriliser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]

    def create(self, validated_data):
        user = User.objects.create(email=validated_data['username'],
                                       name=validated_data['name']
                                         )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserManageSerialiser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email','last_name','first_name','country','rule']



class UserLoginSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username', 'password']   

class UserProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    # fields = ['id', 'username','first_name','last_name','email',]
    exclude = ['password',]

class ParticipantSerializer(serializers.ModelSerializer): 
   class Meta:
      model = Participant
      fields = '__all__'
from django.shortcuts import render
from notes.serializers import UserSerializer
from notes.models import User
from rest_framework import generics
from rest_framework.response import Response

# Create your views here.

class UsercreationView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self,request,*args,**kwargs):

        serializer_instance = UserSerializer(data=request.data)

        if serializer_instance.is_valid():

            data = serializer_instance.validated_data

            User.objects.create_user(**data)

            return Response(data=serializer_instance.data)
        
        else:
            return Response(serializer_instance.errors)
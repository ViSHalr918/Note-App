from rest_framework import serializers
from notes.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","username","email","password","phone"]
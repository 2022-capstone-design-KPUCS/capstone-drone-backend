from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        # call create_user on user object. Without this
        # the password will be stored in plain text.
        return User.objects.create_user(**validated_data)

    
    
    class Meta:
        model = User
        fields = ('auth_token', 'token')
        read_only_fields = ('auth_token',)

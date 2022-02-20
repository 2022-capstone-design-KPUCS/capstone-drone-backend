from rest_framework import serializers

from .models import Administrator, Flight, Deck, Drone


class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = ('id', 'username', 'first_name', 'last_name', )
        read_only_fields = ('username',)

class CreateAdministratorSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        # call create_user on administrator object. Without this
        # the password will be stored in plain text.
        admin = Administrator.objects.create_user(**validated_data)
        return admin

    class Meta:
        model = Administrator
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'email', 'auth_token',)
        read_only_fields = ('auth_token',)
        extra_kwargs = {'password': {'write_only': True}}


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

class CreateFlightSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Flight.objects.create(**validated_data)
    class Meta:
        model = Flight
        fields = '__all__'


class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = '__all__'

class CreateDeckSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Deck.objects.create(**validated_data)
    class Meta:
        model = Deck
        fields = '__all__'


class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = '__all__'


class CreateDroneSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Drone.objects.create(**validated_data)
    class Meta:
        model = Drone
        fields = '__all__'

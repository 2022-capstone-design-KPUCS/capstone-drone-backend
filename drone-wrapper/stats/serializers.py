from rest_framework import serializers

from .models import Administrator, Flight, Deck, Drone


class AdministratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrator
        fields = ('id', 'username', 'password')


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ('id', 'flight_record_url', 'start_time', 'end_time', 'flight_path', 'flight_status')


class DeckSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deck
        fields = ('id', 'deck_name', 'deck_status')


class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = ('id', 'admin_id', 'destination', 'flight', 'deck')
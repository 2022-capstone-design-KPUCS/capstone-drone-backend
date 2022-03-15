from rest_framework import serializers

from .models import Flight, Deck, Drone, FlightRecord

class FlightSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Flight.objects.create(**validated_data)

    class Meta:
        model = Flight
        fields = '__all__'


class DeckSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Deck.objects.create(**validated_data)

    class Meta:
        model = Deck
        fields = '__all__'

class DroneSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Drone.objects.create(**validated_data)

    class Meta:
        model = Drone
        fields = '__all__'
class FlightRecordSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return FlightRecord.objects.create(**validated_data)

    class Meta:
        model = FlightRecord
        fields = '__all__'

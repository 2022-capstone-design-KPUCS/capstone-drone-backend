from rest_framework import serializers

from .models import Flight, Deck, Drone, FlightRecord

class DeckSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Deck.objects.create(**validated_data)

    class Meta:
        model = Deck
        fields = '__all__'

class FlightRecordSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return FlightRecord.objects.create(**validated_data)

    class Meta:
        model = FlightRecord
        fields = '__all__'

class FlightSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Flight.objects.create(**validated_data)

    class Meta:
        model = Flight
        fields = '__all__'


class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = '__all__'

    def create(self, validated_data):
        drone_alias = validated_data['drone_alias'].lower()
        deck_name = "".join([drone_alias, '-deck'])
        Deck.objects.create(deck_name=deck_name, is_occupied=False)
        validated_data['deck'] = Deck.objects.get(deck_name=deck_name)
        validated_data['admin'] = self.context['request'].user
        drone = Drone.objects.create(**validated_data)
        return drone


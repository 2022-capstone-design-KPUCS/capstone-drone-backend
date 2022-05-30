from rest_framework import serializers

from .models import Flight, Drone, FlightRecord

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
        Flight.objects.create(flight_path="", admin=self.context['request'].user)
        validated_data['flight'] = Flight.objects.get(admin=self.context['request'].user)
        validated_data['admin'] = self.context['request'].user
        drone = Drone.objects.create(**validated_data)
        return drone


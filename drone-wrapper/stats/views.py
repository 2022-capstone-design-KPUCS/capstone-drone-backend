from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .permissions import IsUserOrReadOnly
from .models import Flight, Deck, Drone, FlightRecord
from .serializers import FlightSerializer, DeckSerializer, DroneSerializer, FlightRecordSerializer


class DroneViewSet(viewsets.ModelViewSet):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    permission_classes = [IsAuthenticated]


class DeckViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    permission_classes = [IsAuthenticated]


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAuthenticated]

class FlightRecordViewSet(viewsets.ModelViewSet):
    queryset = FlightRecord.objects.all()
    serializer_class = FlightRecordSerializer
    permission_classes = [IsAuthenticated]

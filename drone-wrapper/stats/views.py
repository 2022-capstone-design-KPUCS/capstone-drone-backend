from rest_framework import viewsets
from .permissions import IsUserOrReadOnly
from .models import Flight, Deck, Drone, FlightRecord
from .serializers import FlightSerializer, DeckSerializer, DroneSerializer, FlightRecordSerializer


class DroneViewSet(viewsets.ModelViewSet):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    permission_classes = [IsUserOrReadOnly]


class DeckViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    permission_classes = [IsUserOrReadOnly]


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsUserOrReadOnly]

class FlightRecordViewSet(viewsets.ModelViewSet):
    queryset = FlightRecord.objects.all()
    serializer_class = FlightRecordSerializer
    permission_classes = [IsUserOrReadOnly]

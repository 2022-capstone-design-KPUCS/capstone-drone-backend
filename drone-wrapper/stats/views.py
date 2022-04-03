from rest_framework import viewsets
import django_filters.rest_framework
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView
from .permissions import IsUserOrReadOnly
from .models import Flight, Deck, Drone, FlightRecord
from .serializers import FlightSerializer, DeckSerializer, DroneSerializer, FlightRecordSerializer


class DroneViewSet(ListCreateAPIView, viewsets.GenericViewSet):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)

    def get_queryset(self):
        user = self.request.user
        return Drone.objects.filter(admin_id=user)


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

from rest_framework import viewsets
import django_filters.rest_framework
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import ReadOnly
from .models import Flight, Deck, Drone, FlightRecord
from .serializers import FlightSerializer, DeckSerializer, DroneSerializer, FlightRecordSerializer


class DroneViewSet(viewsets.ModelViewSet):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)

    def get_queryset(self):
        print("USER", self.request.user)
        if self.request.user == 'AnonymousUser':
            user = self.request.user
            filtered_content = Drone.objects.filter(admin_id=user)
        else:
            filtered_content = Drone.objects.all()
        return filtered_content




class DeckViewSet(viewsets.ModelViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class FlightRecordViewSet(viewsets.ModelViewSet):
    queryset = FlightRecord.objects.all()
    serializer_class = FlightRecordSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

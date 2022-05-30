from rest_framework import viewsets
import django_filters.rest_framework
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import ReadOnly
from .models import Flight, Drone, FlightRecord
from .serializers import FlightSerializer, DroneSerializer, FlightRecordSerializer


class DroneViewSet(viewsets.ModelViewSet):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)

    def get_queryset(self):
        print("USER", self.request)
        if self.request.user == 'AnonymousUser':
            filtered_content = Drone.objects.all()
        else:
            user = self.request.user
            filtered_content = Drone.objects.filter(admin=user)
        return filtered_content


class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        print("USER", self.request)
        if self.request.user == 'AnonymousUser':
            filtered_content = Flight.objects.all()
        else:
            user = self.request.user
            filtered_content = Flight.objects.filter(admin=user)
        return filtered_content

class FlightRecordViewSet(viewsets.ModelViewSet):
    queryset = FlightRecord.objects.all()
    serializer_class = FlightRecordSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

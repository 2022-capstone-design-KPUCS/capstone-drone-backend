from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .permissions import IsUserOrReadOnly
from .models import Flight, Deck, Drone, FlightRecord
from .serializers import FlightSerializer, DeckSerializer, DroneSerializer, FlightRecordSerializer
from .serializers import CreateFlightSerializer, CreateDeckSerializer, CreateDroneSerializer, CreateFlightRecordSerializer

"""
    ViewSet Classes:
    - RetrieveModelMixin: Returns an existing model instance
    - UpdateModelMixin: Updates and saves an existing model instance
    - DestroyModelMixin: Deletes an existing model instance
"""
class DroneViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
class FlightViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
class FlightRecordViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = FlightRecord.objects.all()
    serializer_class = FlightRecordSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

class DeckViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


"""
    *** CreateViewSet Classes ***
    - CreateModelMixin: Creates a new model instance.
    - ListModelMixin: Returns a list of all the existing objects.
"""


class DeckCreateViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Deck.objects.all()
    serializer_class = CreateDeckSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class DroneCreateViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Drone.objects.all()
    serializer_class = CreateDroneSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class FlightRecordCreateViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = FlightRecord.objects.all()
    serializer_class = CreateFlightRecordSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class FlightCreateViewSet(mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Flight.objects.all()
    serializer_class = CreateFlightSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

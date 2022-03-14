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


class FlightViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (AllowAny,)


class FlightCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Flight.objects.all()
    serializer_class = CreateFlightSerializer
    permission_classes = (AllowAny,)


class DeckViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Deck.objects.all()
    serializer_class = DeckSerializer
    permission_classes = (AllowAny,)


class DeckCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Deck.objects.all()
    serializer_class = CreateDeckSerializer
    permission_classes = (AllowAny,)


class DroneViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    permission_classes = (AllowAny,)


class DroneCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Drone.objects.all()
    serializer_class = CreateDroneSerializer
    permission_classes = (AllowAny,)


class FlightRecordViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = FlightRecord.objects.all()
    serializer_class = FlightRecordSerializer
    permission_classes = (AllowAny,)


class FlightRecordCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = FlightRecord.objects.all()
    serializer_class = CreateFlightRecordSerializer
    permission_classes = (AllowAny,)
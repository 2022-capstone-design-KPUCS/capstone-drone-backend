from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from rest_framework.parsers import JSONParser
from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .permissions import IsUserOrReadOnly
from .models import Administrator, Flight, Deck, Drone
from .serializers import AdministratorSerializer, FlightSerializer, DeckSerializer, DroneSerializer
from .serializers import CreateAdministratorSerializer, CreateFlightSerializer, CreateDeckSerializer, CreateDroneSerializer

class AdministratorViewSet(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Administrator.objects.all()
    serializer_class = AdministratorSerializer
    permission_classes = (IsUserOrReadOnly,)

class AdministratorCreateViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Administrator.objects.all()
    serializer_class = CreateAdministratorSerializer
    permission_classes = (IsUserOrReadOnly,)


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


class DroneCreateViewSet(mixins.CreateModeMixin, viewsets.GenericViewSet):
    queryset = Drone.objects.all()
    serializer_class = CreateDroneSerializer
    permission_classes = (AllowAny,)
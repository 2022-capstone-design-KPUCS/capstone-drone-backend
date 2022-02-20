import uuid
from pyexpat import model
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from ..users.models import User
class Flight(models.Model):
    """
    A model of flight instances. Records of each flight information.
    드론 비행 정보 인스턴스의 모델. 모든 비행 정보의 기록.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    flight_record_url = models.URLField(max_length=200)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    flight_path = models.TextField(null=True) # JSON-serialized (text) version of your list
    flight_status = models.BooleanField()


class Deck(models.Model):
    """
    A model of deck objects.
    덱 객체의 모델.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    deck_name = models.CharField(max_length=200)
    deck_status = models.BooleanField()


class Drone(models.Model):
    """
    A model of drone objects.
    드론 객체의 모델.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    admin_id = models.ForeignKey(User, on_delete=models.CASCADE)
    surveilance_area = models.TextField(null=True) # JSON-serialized (text) version of list of lat, lng decimals
    flight = models.ManyToManyField(Flight)
    deck = models.ManyToManyField(Deck)

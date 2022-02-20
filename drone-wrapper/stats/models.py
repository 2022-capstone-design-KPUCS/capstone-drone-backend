import uuid
from pyexpat import model
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token

class Administrator(AbstractUser):
    """
    A model of user who can log into the admin interface. Essentially different from django admin user.
    장고 어드민 사용자와는 다른 사용자입니다. 드론 관리자 인터페이스에 로그인 할 수 있는 관리자 사용자 모델 입니다.
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    def __str__(self):
        return self.username

@receiver(post_save, sender=settings.AUTH_ADMIN_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

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
    admin_id = models.ForeignKey(Administrator, on_delete=models.CASCADE)
    surveilance_area = models.TextField(null=True) # JSON-serialized (text) version of list of lat, lng decimals
    flight = models.ManyToManyField(Flight)
    deck = models.ManyToManyField(Deck)

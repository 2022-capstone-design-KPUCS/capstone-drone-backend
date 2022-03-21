from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import User
from .permissions import IsUserOrReadOnly
from .serializers import UserSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_class = (IsUserOrReadOnly,)
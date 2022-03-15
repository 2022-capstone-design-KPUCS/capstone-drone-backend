from doctest import REPORT_ONLY_FIRST_FAILURE
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import User
from .permissions import IsUserOrReadOnly
from .serializers import CreateUserSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsUserOrReadOnly, )

# class UserViewSet(mixins.RetrieveModelMixin,
#                   mixins.UpdateModelMixin,
#                   mixins.DestroyModelMixin,
#                   viewsets.GenericViewSet):
#     """
#     Updates and retrieves user accounts
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsUserOrReadOnly,)

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
        
#     def delete(self, request, *args, **kwargs):
#         return self.delete(request, *args, **kwargs)

# class UserCreateViewSet(mixins.CreateModelMixin,
#                         mixins.ListModelMixin,
#                         viewsets.GenericViewSet):
#     """
#     Creates user accounts
#     """
#     queryset = User.objects.all()
#     serializer_class = CreateUserSerializer
#     permission_classes = (AllowAny,)

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    

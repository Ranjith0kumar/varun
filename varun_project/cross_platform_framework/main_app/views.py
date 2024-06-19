from rest_framework import viewsets
from .models import *
from .serializers import *

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class VersionControlViewSet(viewsets.ModelViewSet):
    queryset = VersionControl.objects.all()
    serializer_class = VersionControlSerializer

class DatabaseConfigViewSet(viewsets.ModelViewSet):
    queryset = DatabaseConfig.objects.all()
    serializer_class = DatabaseConfigSerializer

class ApplicationViewSet(viewsets.ModelViewSet):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer

class UIComponentViewSet(viewsets.ModelViewSet):
    queryset = UIComponent.objects.all()
    serializer_class = UIComponentSerializer

class BackendServiceViewSet(viewsets.ModelViewSet):
    queryset = BackendService.objects.all()
    serializer_class = BackendServiceSerializer

class MobileAppViewSet(viewsets.ModelViewSet):
    queryset = MobileApp.objects.all()
    serializer_class = MobileAppSerializer

class WebComponentViewSet(viewsets.ModelViewSet):
    queryset = WebComponent.objects.all()
    serializer_class = WebComponentSerializer

class DeploymentConfigViewSet(viewsets.ModelViewSet):
    queryset = DeploymentConfig.objects.all()
    serializer_class = DeploymentConfigSerializer

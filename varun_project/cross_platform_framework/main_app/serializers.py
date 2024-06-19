from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class VersionControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = VersionControl
        fields = '__all__'

class DatabaseConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = DatabaseConfig
        fields = '__all__'

class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = '__all__'

class UIComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UIComponent
        fields = '__all__'

class BackendServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = BackendService
        fields = '__all__'

class MobileAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobileApp
        fields = '__all__'

class WebComponentSerializer(serializers.ModelSerializer):
    class Meta:
        model = WebComponent
        fields = '__all__'

class DeploymentConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeploymentConfig
        fields = '__all__'

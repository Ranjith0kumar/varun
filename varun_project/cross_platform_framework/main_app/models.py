from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    password_hash = models.CharField(max_length=256)
    email = models.EmailField(unique=True)

class VersionControl(models.Model):
    version_control_type = models.CharField(max_length=50)
    repository_url = models.URLField()
    credentials = models.CharField(max_length=256)

class DatabaseConfig(models.Model):
    database_type = models.CharField(max_length=50)
    connection_string = models.CharField(max_length=256)
    credentials = models.CharField(max_length=256)

class Application(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    app_name = models.CharField(max_length=100)
    platform = models.CharField(max_length=50)
    version_control = models.OneToOneField(VersionControl, on_delete=models.CASCADE)
    database_config = models.OneToOneField(DatabaseConfig, on_delete=models.CASCADE)

class UIComponent(models.Model):
    component_name = models.CharField(max_length=100)
    component_type = models.CharField(max_length=50)
    component_description = models.TextField()

class BackendService(models.Model):
    service_name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=50)
    service_url = models.URLField()

class MobileApp(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    platform = models.CharField(max_length=50)
    deployment_config = models.OneToOneField('DeploymentConfig', on_delete=models.CASCADE)

class WebComponent(models.Model):
    ui_component = models.ForeignKey(UIComponent, on_delete=models.CASCADE)
    web_component_url = models.URLField()

class DeploymentConfig(models.Model):
    deployment_type = models.CharField(max_length=50)
    deployment_url = models.URLField()
    credentials = models.CharField(max_length=256)

from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'version-control', VersionControlViewSet)
router.register(r'database-config', DatabaseConfigViewSet)
router.register(r'applications', ApplicationViewSet)
router.register(r'ui-components', UIComponentViewSet)
router.register(r'backend-services', BackendServiceViewSet)
router.register(r'mobile-apps', MobileAppViewSet)
router.register(r'web-components', WebComponentViewSet)
router.register(r'deployment-configs', DeploymentConfigViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('mainpage/', views.index, name='index'),
    
    path("userpage/",user_view),
]

# cross_platform/urls.py



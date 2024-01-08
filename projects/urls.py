from rest_framework import routers 
from .api import ProjectViewSet

router = routers.DefaultRouter() 

router.register('api/projects', ProjectViewSet, 'projects')# ruta vieset y nombre

urlpatterns = router.urls
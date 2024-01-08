from .models import Project
from rest_framework import viewsets, permissions 
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all() 
    permission_classes = [permissions.AllowAny ] #permisos 
    serializer_class = ProjectSerializer # se usa lo que ya se creo

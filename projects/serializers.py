from rest_framework import serializers 
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project 
        fields = ('id', 'title', 'description', 'technology', 'created_at') # campos para la api 
        read_only_fields = ('created_at',) # campo que solo se puede leer 
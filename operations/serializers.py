from rest_framework import serializers
from stack_data import Serializer

from operations.models import Operations
from .file import FileCnab

class OperationsSerializer(serializers.ModelSerializer):
    class Meta: 
        model= Operations
        fields= "__all__"
    
  
    
    
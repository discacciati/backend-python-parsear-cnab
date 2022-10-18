from rest_framework import serializers
from stack_data import Serializer

from operations.models import Operations
from .file import FileCnab

class OperationsSerializer(serializers.ModelSerializer):
    class Meta: 
        model= Operations
        fields= "__all__"
    
    def create(self, validated_data): 
        full_file = FileCnab(validated_data.get("file"))
        
        for item in full_file.operations: 
            serializer = OperationsSerializer(data=item)
            serializers.is_valid(raise_exception=True)
            serializer.save()
        
    
    
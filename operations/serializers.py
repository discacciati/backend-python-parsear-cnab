from rest_framework import serializers

from operations.models import Operations

class OperationsSerializer(serializers.ModelSerializer):
    class Meta: 
        model= Operations
        fields= "__all__"
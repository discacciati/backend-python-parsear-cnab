from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView

from .models import Operations
from .serializers import OperationsSerializer

class OperationsView(ListCreateAPIView):
    queryset = Operations.objects.all()
    serializer_class = OperationsSerializer



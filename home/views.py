from rest_framework import viewsets
from rest_framework.response import Response
from .models import Home
from home.serializers import HomeSerializer

# Create your views here.
class HomeAPI(viewsets.ModelViewSet):
  queryset = Home.objects.all()
  serializer_class = HomeSerializer

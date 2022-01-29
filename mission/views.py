from rest_framework import viewsets
from rest_framework.response import Response
from .models import Mission
from .serializers import MissionSerializer

# Create your views here.
class MissionAPI(viewsets.ModelViewSet):
  queryset = Mission.objects.all()
  serializer_class = MissionSerializer
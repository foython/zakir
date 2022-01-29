from rest_framework import viewsets
from .serializers import VisionSerializer
from .models import Vision


# Create your views here.
class VisionAPI(viewsets.ModelViewSet):
  queryset = Vision.objects.all()
  serializer_class = VisionSerializer

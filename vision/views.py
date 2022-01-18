from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import VisionSerializer
from .models import Vision
from rest_framework.response import Response

# Create your views here.
class VisionAPI(APIView):

  def get(self, request, pk=None):
    id = pk
    if id is not None:
      vision = Vision.objects.get(id=id)
      serializer = VisionSerializer(vision)
      return Response(serializer.data)

    vision = Vision.objects.all()
    serializer = VisionSerializer(vision, many=True)
    return Response(serializer.data)

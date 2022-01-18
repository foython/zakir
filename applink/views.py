from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import AppLinkSerializer
from .models import AppLink
from rest_framework.response import Response

# Create your views here.
class AppAPI(APIView):

  def get(self, request, pk=None):
    id = pk
    if id is not None:
      app = AppLink.objects.get(id=id)
      serializer = AppLinkSerializer(app)
      return Response(serializer.data)

    app = AppLink.objects.all()
    serializer = AppLinkSerializer(app, many=True)
    return Response(serializer.data)
from rest_framework.views import APIView
from rest_framework.response import Response
from home.models import Home
from home.serializers import HomeSerializer

# Create your views here.
class HomeAPI(APIView):

  def get(self, request, pk=None, format=None):
    id = pk
    if id is not None:
      home = Home.objects.get(id=id)
      serializer = HomeSerializer(home)
      return Response(serializer.data)

    home = Home.objects.all()
    serializer = HomeSerializer(home, many=True)
    return Response(serializer.data)
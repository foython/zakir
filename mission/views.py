from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Mission
from .serializers import MissionSerializer

# Create your views here.
class MissionAPI(APIView):

  def get(self, request, pk=None):
    id = pk
    if id is not None:
      mission = Mission.objects.get(id=id)
      serilizer = MissionSerializer(mission)
      return Response(serilizer.data)

    mission = Mission.objects.all()
    serilizer = MissionSerializer(mission, many=True)
    return Response(serilizer.data)
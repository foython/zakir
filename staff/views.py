from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import StaffSerializer
from .models import Staff
from rest_framework.response import Response

# Create your views here.
class StaffAPI(APIView):

  def get(self, request, pk=None):
    id = pk
    if id is not None:
      staff = Staff.objects.get(id=id)
      serializer = StaffSerializer(staff)
      return Response(serializer.data)

    staff = Staff.objects.all()
    serializer = StaffSerializer(staff, many=True)
    return Response(serializer.data)
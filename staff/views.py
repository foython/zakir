from rest_framework import viewsets
from .serializers import StaffSerializer
from .models import Staff


# Create your views here.
class StaffAPI(viewsets.ModelViewSet):
  queryset = Staff.objects.all()
  serializer_class = StaffSerializer
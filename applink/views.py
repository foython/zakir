from rest_framework import viewsets
from .serializers import AppLinkSerializer
from .models import AppLink


# Create your views here.
class AppLinkAPI(viewsets.ModelViewSet):
  queryset = AppLink.objects.all()
  serializer_class = AppLinkSerializer

from rest_framework import viewsets
from .serializers import OfferSerializer
from .models import Offer


# Create your views here.
class OfferAPI(viewsets.ModelViewSet):
  queryset = Offer.objects.all()
  serializer_class = OfferSerializer

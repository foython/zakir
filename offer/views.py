from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import OfferSerializer
from .models import Offer
from rest_framework.response import Response

# Create your views here.
class OfferAPI(APIView):

  def get(self, request, pk=None):
    id = pk
    if id is not None:
      offer = Offer.objects.get(id=id)
      serializer = OfferSerializer(offer)
      return Response(serializer.data)

    offer = Offer.objects.all()
    serializer = OfferSerializer(offer, many=True)
    return Response(serializer.data)

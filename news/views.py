from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import NewsSerializer
from news.models import News 
from rest_framework.response import Response

# Create your views here.
class NewsAPI(APIView):

  def get(self, request, pk=None):
    id = pk
    if id is not None:
      news = News.objects.get(id=id)
      serializer = NewsSerializer(news)
      return Response(serializer.data)

    news = News.objects.all()
    serializer = NewsSerializer(news, many=True)
    return Response(serializer.data)
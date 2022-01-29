from rest_framework import viewsets
from .serializers import NewsSerializer
from .models import News 


# Create your views here.
class NewsAPI(viewsets.ModelViewSet):
  queryset = News.objects.all()
  serializer_class = NewsSerializer
      
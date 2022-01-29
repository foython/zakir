from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


#creat Router Object
router = DefaultRouter()

#REgester views with Router
router.register('api', views.HomeAPI, basename='home')


urlpatterns = [
    path('', include(router.urls)),    
]
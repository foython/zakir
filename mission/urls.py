from django.urls import path
from . import views


urlpatterns = [
    path('api/', views.MissionAPI.as_view()),
    path('api/<int:pk>', views.MissionAPI.as_view()),    
]
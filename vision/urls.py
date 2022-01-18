from django.urls import path
from . import views


urlpatterns = [
    path('api/', views.VisionAPI.as_view()),
    path('api/<int:pk>', views.VisionAPI.as_view()),    
]
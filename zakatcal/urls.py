from django.urls import path
from . import views


urlpatterns = [
    path('api/', views.HomeAPI.as_view()),
    path('api/<int:pk>', views.HomeAPI.as_view()),    
]
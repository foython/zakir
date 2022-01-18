from django.urls import path
from . import views


urlpatterns = [
    path('api/', views.NewsAPI.as_view()),
    path('api/<int:pk>', views.NewsAPI.as_view()),    
]
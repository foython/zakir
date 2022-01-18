from django.urls import path
from . import views


urlpatterns = [
    path('api/', views.AppAPI.as_view()),
    path('api/<int:pk>', views.AppAPI.as_view()),    
]
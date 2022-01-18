from django.urls import path
from . import views


urlpatterns = [
    path('api/', views.StaffAPI.as_view()),
    path('api/<int:pk>', views.StaffAPI.as_view()),    
]
from django.urls import path
from . import views


urlpatterns = [
    path('api/', views.OfferAPI.as_view()),
    path('api/<int:pk>', views.OfferAPI.as_view()),    
]
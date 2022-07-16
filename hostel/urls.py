from django.urls import path
from .views import *



urlpatterns = [
    path('hostals/', hostalsList.as_view()),
    path('hostals/<int:pk>',hostalsListone.as_view()),
    path('registerHostel',registerHostel.as_view()),
    path('hsotelsOfanOwner/<int:pk>',fetchHostels.as_view()),



]

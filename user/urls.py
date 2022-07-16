from django.urls import path
from .views import *

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('Food_Hostel_PG', select_Food_Hostel_PG.as_view(), name='home'),
    path('api/token/', MyTokenObtainPaiView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('Hostel/<int:hostel_id>', singleItemForHostel.as_view(), name='SingleHostel'),
    path('HostelImage/<int:hostel_id>', getHostelImages.as_view(), name='HostelImage'),
    path('TopRooms', getTopRooms.as_view(), name='TopRooms'),
    ]

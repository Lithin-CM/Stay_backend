from .models import *
from hostel.models import *
from rest_framework.views import APIView
from .serializers import *
from hostel.serializers import *

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet 
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView

# Create your views here.

class MyTokenObtainPaiView(TokenObtainPairView):
    serializer_class=MyTokenObtainPairSerializer



class user_register(ModelViewSet): 
    serializer_class = UserRegistrationSerializer
    queryset = UserRegistration.objects.all()



class select_Food_Hostel_PG(APIView):
    def get(self,request):
        hostels = Hostels.objects.all()
        serializer = HostelSerializer(hostels,many = True)
        print(serializer.data)
        return Response(serializer.data,status=status.HTTP_200_OK)
    


class singleItemForHostel(APIView):
    
    def get(self,request,hostel_id):
        hostel = Hostels.objects.get(id=hostel_id)
        serializer = HostelSerializer(hostel)
        print(serializer.data)
        return Response(serializer.data,status=status.HTTP_200_OK)



class getHostelImages(APIView):
    def get(self,request,hostel_id):
        hostel_images = HostelImages.objects.filter(hostel = hostel_id)
        serializer = HostelImageSerializer(hostel_images,many =True)
        return Response(serializer.data,status=status.HTTP_200_OK)



class getTopRooms(APIView):
    def get(self,request):
        TopRooms = Rooms.objects.all()
        serializer = HostelRoomSerializer(TopRooms,many =True)
        return Response(serializer.data,status=status.HTTP_200_OK)

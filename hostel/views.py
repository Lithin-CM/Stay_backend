from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated,AllowAny

# Create your views here.
from .models import *
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

from rest_framework.viewsets import ModelViewSet 

# Create your views here.

class hostalsList(APIView):
    def get(self,request):
        hostal = Hostels.objects.all()
        serializers = HostelSerializer(hostal,many =True )
        return Response(serializers.data)



    def post(self,request):
        serializer = HostelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.error)



class hostalsListone(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,pk):
        hostal = Hostels.objects.get(id = pk)
        serializers = HostelSerializer(hostal)
        return Response(serializers.data)

    def put(self,request,pk):
        hostal = Hostels.objects.get(id = pk)
        serializers = HostelSerializer(hostal,data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)
    def delete(self,request,pk):
        Hostels.objects.filter(id = pk).delete()
        return Response({})



class registerHostel(APIView):
    def post(self, request):
        print(request.data,"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        serailzer = HostelSerializer(data=request.data)
        if serailzer.is_valid():
            print("data2")
            serailzer.save()
            return Response({}, status=status.HTTP_201_CREATED)
        else:
            print(serailzer.errors)
            return Response(serailzer.errors, status=status.HTTP_400_BAD_REQUEST)




class fetchHostels(APIView):
    def get(self,request,pk):
        hostal = Hostels.objects.filter(owner = pk)
        serializers = HostelSerializer(hostal, many = True)
        return Response(serializers.data)
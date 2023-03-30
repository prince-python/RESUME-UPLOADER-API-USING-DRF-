from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from . models import *
from rest_framework.response import Response
from rest_framework import status



class ProfileView(APIView):
    def post(self,request,format=None):
        serializer=ProfileSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Resume uploaded succesfully','status':'success','candidate':serializer.data}
                            ,status=status.HTTP_201_CREATED)
        return Response (serializer.errors)
        


    def get(self,request,format=None):
        candidates=Profile.objects.all()
        serializer= ProfileSerializers(candidates,many=True)
        return Response({'status':'succes','candidates':serializer.data},status=status.HTTP_200_OK)
    
    
    
    def delete(self,request,format=None):
        candidates=Profile.objects.all()
        return Response ({'status':'success'})
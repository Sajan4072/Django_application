from unittest import result
from django.shortcuts import render
from .forms import InputForm
from .models import Fare
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import InputSerializer
from rest_framework.decorators import api_view




# Create your views here.

def HomeView(request):
    form=InputForm()
    return render(request,'home/index.html',{'form':form})

'''view to calculate fare'''
@api_view(['POST'])
def CalculateView(request,*args,**kwargs):
    serializer=InputSerializer(data=request.POST)
    if serializer.is_valid(raise_exception=True):
        time=serializer.validated_data.get('time')
        distance=serializer.validated_data.get('distance')
        result=Fare.calculate_fares(time,distance)        
        return Response(result,status=200)
    return Response({},status=400) 


   
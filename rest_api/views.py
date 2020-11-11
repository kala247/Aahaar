from django.shortcuts import render
from bhojan.models import Partymenu
from rest_api.serializers import BhojanSerializer, BhojanpicSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from rest_framework import decorators


# Create your views here.

class BhojanViewset(viewsets.ModelViewSet):
    serializer_class = BhojanSerializer
    queryset = Partymenu.objects.all()

    @decorators.action(
        detail = True,
        methods = ['PUT'],
        serializer_class = BhojanpicSerializer,
        parser_classes = [MultiPartParser],
    )

    def img(self,request,pk):
        obj = self.get_object()
        serializer = self.serializer_class(obj,data = request.data,partial = True)

        if serializer.is_vallid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)



















@api_view(["GET","POST"])
def bhojan_list(request):
    if request.method=="GET":
        menu = Partymenu.objects.all()
        serializer = BhojanSerializer(menu,many=True)
        return Response(serializer.data)
    
    elif request.method == "POST":
        serializer = BhojanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","DELETE"])
def bhojan_details(request,id):

    try:
        menu = Partymenu.objects.get(id=id)
    except Partymenu.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = BhojanSerializer(menu)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    elif request.method == "PUT":
        serializer = BhojanSerializer(menu,data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        menu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
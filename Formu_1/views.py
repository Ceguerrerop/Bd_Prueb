from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import MiModelo
from .serializers import MiModeloSerializer

class MiVista(APIView):
    def post(self, request):
        serializer = MiModeloSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


def get_uploaded_info(request):
    info = MiModelo.objects.all()
    data = [{'id': i.id, 'name': i.name, 'file': i.file.url} for i in info]
    return JsonResponse(data, safe=False)
    


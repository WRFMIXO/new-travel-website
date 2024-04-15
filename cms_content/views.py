from django.shortcuts import render
from .serializers import TextContentSerializer, MediaContentSerializer
from .models import TextContent, MediaContent
from rest_framework import generics

# Create your views here.
class CreateTextContentView(generics.CreateAPIView):
    queryset = TextContent.objects.all()
    serializer_class = TextContentSerializer

class CreateMediaContentView(generics.CreateAPIView):
    queryset = MediaContent.objects.all()
    serializer_class = MediaContentSerializer

class ListTextContentView(generics.ListAPIView):
    queryset = TextContent.objects.all()
    serializer_class = TextContentSerializer

class ListMediaContentView(generics.ListAPIView):
    queryset = MediaContent.objects.all()
    serializer_class = MediaContentSerializer
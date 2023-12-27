from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from restaurant.models import Menu, Booking  

# Create your views here.
def home(request):
    return render(request, 'index.html')

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
from django.shortcuts import get_object_or_404, render
from rest_framework.response import Response
from .serializers import *
from restaurant.models import Menu, Booking  
from rest_framework import viewsets, generics 
from rest_framework import permissions
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def home(request):
    return render(request, 'index.html')

class MenuItemView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Menu.objects.all()
    serializer_class = MenuItemSerializer
    

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = MenuItemSerializer 
    permission_classes = [IsAuthenticated]
    
       

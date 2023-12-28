from django.test import TestCase
from restaurant.models import Menu
from django.test import Client


from restaurant.serializers import MenuItemSerializer
from restaurant.views import MenuItemView


class MenuViewTest(TestCase):
    
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    
    def test_getItem(self):
        response = self.client.get('/menu/1/')
    
    def test_getall(self):
        response = self.client.get('/menu/')
        
        
        
        
        

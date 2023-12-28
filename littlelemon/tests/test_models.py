from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="test", price=10, inventory=10)
        
        self.assertEqual(item, Menu.objects.get(title="test", price=10, inventory=10))

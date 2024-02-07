from django.test import TestCase
from restaurant.models import MenuItem

class MenuViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="Item 1", price=5, inventory=100)
        MenuItem.objects.create(title="Item 2", price=6, inventory=100)
        MenuItem.objects.create(title="Item 3", price=7, inventory=100)
        
    def test_getall(self):
        items = MenuItem.objects.all()
        print(items)
        self.assertEqual(str(items[0]), "Item 1 : 5.00")
        self.assertEqual(str(items[1]), "Item 2 : 6.00")
        self.assertEqual(str(items[2]), "Item 3 : 7.00")
        
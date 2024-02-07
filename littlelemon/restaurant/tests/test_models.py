from django.test import TestCase
from restaurant.models import MenuItem

class MenuTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="Ice cream", price=2.99, inventory=100)
    
        self.assertEqual(str(item), "Ice cream : 2.99")
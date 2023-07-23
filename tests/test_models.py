from django.test import TestCase
from restaurant.models import Menu

class MenuItemTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="IceCream", price=80, inventory=100)
    def test_get_item(self):
        item = Menu.objects.get(title="IceCream")
        self.assertEqual(item.price, 80)
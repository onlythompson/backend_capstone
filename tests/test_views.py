from django.test import TestCase
from restaurant import views
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create\
        (title="Strawberry IceCream", price=45, inventory=100)
    
    # def test_getall(self):
    #     response = views.BookingViewSet()
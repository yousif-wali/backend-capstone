from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Menu  
from ..serializers import MenuSerializer 

class MenuViewTest(TestCase):
    def setUp(self):
        self.menu1 = Menu.objects.create(title="Pizza", price=10.99, inventory=100)
        self.menu2 = Menu.objects.create(title="Burger", price=8.99, inventory=100)
        self.menu3 = Menu.objects.create(title="Salad", price=6.99, inventory=100)

    def test_getall(self):
        response = self.client.get(reverse('menu-list'))
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)



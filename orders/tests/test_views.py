from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from orders.models import Order


class OrderViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='pass123')
        self.staff = User.objects.create_user(username='staff', password='pass123', is_staff=True)

    def test_orders_list_anonymous_redirect(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)  # redirect to login

    def test_orders_list_authenticated(self):
        self.client.login(username='testuser', password='pass123')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_order_create(self):
        self.client.login(username='testuser', password='pass123')
        response = self.client.post(reverse('order_create'), {
            'order_type': 'single',
            'name': 'Тестовый заказ',
            'description': 'Описание'
        })
        self.assertEqual(response.status_code, 302)  # redirect после успеха
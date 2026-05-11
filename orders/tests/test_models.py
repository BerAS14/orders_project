from django.test import TestCase
from django.contrib.auth.models import User
from orders.models import Order
from datetime import date


class OrderModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')

    def test_order_creation(self):
        order = Order.objects.create(
            user=self.user,
            order_type='single',
            name='Тестовый заказ',
            description='Описание тестового заказа'
        )
        self.assertTrue(order.order_number.startswith('ORD-'))
        self.assertEqual(order.status, 'created')
        self.assertEqual(str(order), f"{order.order_number} — Тестовый заказ")

    def test_ready_date_auto_set(self):
        order = Order.objects.create(
            user=self.user,
            order_type='single',
            name='Готовый заказ',
            status='ready'
        )
        self.assertIsNotNone(order.ready_date)
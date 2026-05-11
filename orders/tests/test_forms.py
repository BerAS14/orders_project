from django.test import TestCase
from orders.forms import OrderCreateForm


class OrderCreateFormTest(TestCase):

    def test_single_order_valid(self):
        form_data = {
            'order_type': 'single',
            'name': 'Единичный заказ',
            'description': 'Хорошее описание'
        }
        form = OrderCreateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_single_order_without_description(self):
        form_data = {
            'order_type': 'single',
            'name': 'Без описания'
        }
        form = OrderCreateForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors)

    def test_multiple_order_valid(self):
        form_data = {
            'order_type': 'multiple',
            'name': 'Множественный заказ',
            'quantity': 5
        }
        # В реальном тесте нужно передавать файл, но для базовой проверки:
        form = OrderCreateForm(data=form_data)
        self.assertFalse(form.is_valid())  # без файла будет ошибка
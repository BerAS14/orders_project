from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):

    class Meta:
        model = Order

        fields = [
            'order_type',
            'name',
            'description',
            'document',
            'quantity',
        ]

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите наименование заказа',
            }),

            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Введите описание заказа',
            }),

            'quantity': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите количество',
            }),
        }

    def clean(self):

        cleaned_data = super().clean()

        order_type = cleaned_data.get('order_type')

        description = cleaned_data.get('description')

        document = cleaned_data.get('document')

        quantity = cleaned_data.get('quantity')

        # SINGLE
        if order_type == 'single':

            if not description:

                self.add_error(
                    'description',
                    'Для единичного заказа заполните описание.'
                )

            cleaned_data['document'] = None
            cleaned_data['quantity'] = None

        # MULTIPLE
        elif order_type == 'multiple':

            if not document:

                self.add_error(
                    'document',
                    'Прикрепите документ.'
                )

            if not quantity or quantity < 1:

                self.add_error(
                    'quantity',
                    'Укажите корректное количество.'
                )

            cleaned_data['description'] = None

        return cleaned_data
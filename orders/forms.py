from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['order_type', 'name', 'description', 'document', 'quantity']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите наименование заказа'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        order_type = cleaned_data.get('order_type')

        if order_type == 'single':
            if not cleaned_data.get('description'):
                raise forms.ValidationError("Для единичного заказа обязательно заполните описание")
            cleaned_data['document'] = None
            cleaned_data['quantity'] = None

        elif order_type == 'multiple':
            if not cleaned_data.get('document'):
                raise forms.ValidationError("Для множественного заказа обязательно прикрепите документ")
            if not cleaned_data.get('quantity') or cleaned_data.get('quantity') < 1:
                raise forms.ValidationError("Укажите корректное количество")
            cleaned_data['description'] = None

        return cleaned_data
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Order(models.Model):
    STATUS_CHOICES = [
        ('created', 'Создан'),
        ('processing', 'Обрабатывается'),
        ('assembling', 'Собирается'),
        ('delivering', 'Доставляется'),
        ('ready', 'Готов'),
    ]

    TYPE_CHOICES = [
        ('single', 'Единичный'),
        ('multiple', 'Множественный'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name="Пользователь")

    order_number = models.CharField("Номер заказа", max_length=20, unique=True, editable=False)
    order_type = models.CharField("Тип заказа", max_length=10, choices=TYPE_CHOICES)

    name = models.CharField("Наименование заказа", max_length=255)

    # Для единичного заказа
    description = models.TextField("Описание", blank=True, null=True)

    # Для множественного заказа
    document = models.FileField("Документ", upload_to='orders/documents/', blank=True, null=True)
    quantity = models.PositiveIntegerField("Количество", blank=True, null=True)

    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES, default='created')
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    ready_date = models.DateField("Дата готовности", blank=True, null=True)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.order_number} — {self.name}"

    def save(self, *args, **kwargs):
        if not self.order_number:
            # Генерация номера заказа: ORD-0001, ORD-0002 и т.д.
            last_order = Order.objects.order_by('-id').first()
            if last_order and last_order.order_number:
                num = int(last_order.order_number.split('-')[1]) + 1
            else:
                num = 1
            self.order_number = f"ORD-{num:04d}"

        # Автоматически ставим дату готовности при статусе "Готов"
        if self.status == 'ready' and not self.ready_date:
            self.ready_date = timezone.now().date()

        super().save(*args, **kwargs)
from django.urls import path

from orders.views import orders_list, order_create, order_detail

urlpatterns = [
    path('', orders_list, name='home'),
    path('create/', order_create, name='order_create'),
    path('<int:pk>/', order_detail, name='order_detail'),
]
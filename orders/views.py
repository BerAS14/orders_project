from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from orders.forms import OrderCreateForm
from orders.models import Order


@login_required(login_url='login')
def orders_list(request):
    """Главная страница — список заказов"""

    status_filter = request.GET.get('status')

    if request.user.is_staff:
        orders = Order.objects.all().order_by('-created_at')
    else:
        orders = Order.objects.filter(user=request.user).order_by('-created_at')

    if status_filter:
        orders = orders.filter(status=status_filter)

    context = {
        'orders': orders,
        'status_filter': status_filter,
        'status_choices': Order.STATUS_CHOICES,
        'title': 'Мои заказы'
    }

    return render(request, 'orders/orders_list.html', context)


@login_required(login_url='login')
def order_create(request):
    if request.method == 'POST':
        form = OrderCreateForm(request.POST, request.FILES)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()

            messages.success(request, f'Заказ {order.order_number} успешно создан!')
            return redirect('home')  # или 'order_list'
    else:
        form = OrderCreateForm()

    return render(request, 'orders/order_create.html', {'form': form})


@login_required(login_url='login')
def order_detail(request, pk):
    """Просмотр детальной информации о заказе"""
    order = get_object_or_404(Order, pk=pk)

    # Обычный пользователь может видеть только свои заказы
    if not request.user.is_staff and order.user != request.user:
        from django.core.exceptions import PermissionDenied
        raise PermissionDenied

    context = {
        'order': order,
    }
    return render(request, 'orders/order_detail.html', context)
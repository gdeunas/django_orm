from django.shortcuts import render
from .models import Product


def home(request):
    # Выбираем 5 последних продуктов
    latest_products = Product.objects.order_by('-id')[:5]

    # Выводим их в консоль
    print('Вывод 5 последних продуктов:')
    for product in latest_products:
        print(f"id: {product.id}, Название: {product.name}, цена за покупку: {product.price}")

    return render(request, 'catalog/home.html', {'products': latest_products})

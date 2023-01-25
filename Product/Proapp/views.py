
from django.shortcuts import render, get_object_or_404
from .models import ProductMainModel
from django.http import JsonResponse

def get_all_products(request):
    products = ProductMainModel.objects.all()
    product_list = []
    for product in products:
        product_list.append({
            'id': product.id,
            'title': product.title,
            'description': product.description,
            'price': product.price,
            'unique_code': product.unique_code,
            'size': product.size,
        })
    return JsonResponse(product_list, safe=False)

def product_detail(request, product_id):
    product = get_object_or_404(ProductMainModel, id=product_id)
    product_detail = {
        'id': product.id,
        'title': product.title,
        'description': product.description,
        'price': product.price,
        'unique_code': product.unique_code,
        'size': product.size,
    }
    return JsonResponse(product_detail)
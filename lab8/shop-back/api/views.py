from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Product, Category


@require_http_methods(['GET'])


def product_list(request):
    products = Product.objects.all()
    data = []
    for product in products:
        data.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'count': product.count,
            'is_active': product.is_active,
            'category_id': product.category_id,
        })
    return JsonResponse(data, safe=False)


@require_http_methods(['GET'])
def product_detail(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Product not found'}, status=404)

    data = {
        'id': product.id,
        'name': product.name,
        'price': product.price,
        'description': product.description,
        'count': product.count,
        'is_active': product.is_active,
        'category_id': product.category_id,
    }
    return JsonResponse(data)


@require_http_methods(['GET'])
def category_list(request):
    categories = Category.objects.all()
    data = []
    for category in categories:
        data.append({
            'id': category.id,
            'name': category.name,
        })
    return JsonResponse(data, safe=False)


@require_http_methods(['GET'])
def category_detail(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)

    data = {
        'id': category.id,
        'name': category.name,
    }
    return JsonResponse(data)


@require_http_methods(['GET'])
def category_products(request, id):
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        return JsonResponse({'error': 'Category not found'}, status=404)

    products = Product.objects.filter(category=category)
    data = []
    for product in products:
        data.append({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description,
            'count': product.count,
            'is_active': product.is_active,
            'category_id': product.category_id,
        })
    return JsonResponse(data, safe=False)

from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'store/index.html')


def product(request):
    context = {}
    return render(request, 'store/product.html')


def product_detail(request, pk):
    context = {}
    return render(request, 'store/product-detail')

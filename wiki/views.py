from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from .models import Product, Category
from haystack.query import SearchQuerySet


def categories(request):
    data = Category.objects.all()
    context = {"all_categories": data}
    return render(request, "categories.html", context)


def products_of_category(request, category_id):
    category = Category.objects.get(id=category_id)
    products = Product.objects.filter(category_id=category_id)
    context = {
        "category": category,
        "products": products}
    return render(request, "products_of_category.html", context)


def products_all(request):
    data = Product.objects.all()
    context = {"all_products": data}
    return render(request, "products_all.html", context)


def index(request):
    data = Product.objects.all().order_by('-pub_date')[:5]
    context = {"recent_five_products": data}
    return render(request, "index.html", context)


def product(request, product_id):
    data = get_object_or_404(Product, id=product_id)
    product_category = Category.objects.get(id=data.category_id)
    context = {"product": data, "product_category": product_category}
    return render(request, "product.html", context)


def search(request):
    query = request.GET.get('q')
    results = SearchQuerySet().filter(content=query).models(Product)
    context = {"query": query, "results": results}
    return render(request, "search_results.html", context)

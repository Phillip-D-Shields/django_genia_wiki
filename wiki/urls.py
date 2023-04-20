from django.urls import path

from . import views

app_name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("categories/", views.categories, name="categories"),
    path("categories/<int:category_id>/products", views.products_of_category, name="products_of_category"),
    path("products", views.products_all, name="products_all"),
    path("products/<int:product_id>", views.product, name="product"),
    path("search", views.search, name="search"),
]

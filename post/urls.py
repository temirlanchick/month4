from django.urls import path
from post import views

urlpatterns = [
    path('products/create/', views.product_create),
    path('products/', views.products_view),
    path('categories/create', views.category_create),
    path('categories/', views.categories_view)
]

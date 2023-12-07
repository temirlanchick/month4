from django.urls import path
from post import views

urlpatterns = [
    path('products_image/create/', views.product_create),
    path('products_image/', views.products_view),
    path('products/<int:product_id>/', views.product_update_view),
    path('categories/create', views.category_create),
    path('categories/', views.categories_view)
]

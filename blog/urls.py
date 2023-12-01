
from django.contrib import admin
from django.urls import path
from post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('current_date/', views.current_date),
    path('goodbye/', views.goodbye),
    path('', views.main_view),
    path('products/create/', views.product_create),
    path('products/', views.products_view),
    path('categories/create', views.category_create),
    path('categories/', views.categories_view)
]


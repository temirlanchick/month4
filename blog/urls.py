
from django.contrib import admin
from django.urls import path
from post import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello),
    path('current_date/', views.current_date),
    path('goodbye/', views.goodbye),
    path('', views.main_view),
    path('products/', views.products_view)
]


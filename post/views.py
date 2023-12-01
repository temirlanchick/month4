from django.shortcuts import HttpResponse, render, redirect
from post.models import Product, Category
from post.forms import ProductCreateForm, CategoryCreateForm


def hello(request):
    if request.method == 'GET':
        return HttpResponse('Hello! Its my projects')


def current_date(request):
    if request.method == 'GET':
        return HttpResponse('14 november')


def goodbye(request):
    if request.method == 'GET':
        return HttpResponse('Goodbye user')


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/main.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        return render(request, 'products/products.html', context={
            "products": products
        })


def categories_view(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        return render(request, 'categories/categories.html', context={
            "categories": categories
        })


def product_create(request):
    if request.method == 'GET':
        context = {
            "form": ProductCreateForm
        }
        return render(request, 'products/create.html', context)
    if request.method == 'PRODUCT':
        form = ProductCreateForm(request.PRODUCT, request.FILES)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            return redirect("/products/")

        context = {
            "form": form
        }

        return render(request, 'products/create.html', context)


def category_create(request):
    if request.method == 'GET':
        context = {
            "form": CategoryCreateForm
        }
        return render(request, 'categories/create.html', context)
    if request.method == 'CATEGORY':
        form = CategoryCreateForm(request.CATEGORY, request.FILES)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect("/categories/")

        context = {
            "form": form
        }

        return render(request, 'categories/create.html', context)

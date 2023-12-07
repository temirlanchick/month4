from django.shortcuts import HttpResponse, render, redirect
from django.db.models import Q
from post.models import Product, Category
from post.forms import ProductCreateForm, CategoryCreateForm, ProductCreateForm2
from django.conf import settings


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

        search = request.GET.get('search')
        order = request.GET.get('order')

        if search:

            products = products.filter(
                Q(title__icontains=search) |
                Q(content__icontains=search)
            )

        if order == 'title':
            products = products.order_by('title')
        elif order == '-title':
            products = products.order_by('-title')
        elif order == 'created_at':
            products = products.order_by('created_at')
        elif order == '-created_at':
            products = products.order_by('-created_at')

        max_page = products.__len__() / settings.PAGE_SIZE

        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        page = int(request.GET.get('page', 1))

        start = (page - 1) * settings.PAGE_SIZE
        end = page * settings.PAGE_SIZE

        products = products[start:end]

        context = {
            "products": products,
            "pages": range(1, max_page + 1)
        }

        return render(request, 'products_image/products_image.html', context={
            "products_image": products
        })


def products_detail_view(request, product_id):
    if request.method == 'GET':
        try:
            post = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return render(request, 'errors/404.html')

        context = {
            "post": post
        }

        return render(request,
                      'products/detail.html',
                      context)


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
        return render(request, 'products_image/create.html', context)
    if request.method == 'PRODUCT':
        form = ProductCreateForm(request.PRODUCT, request.FILES)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
            return redirect("/products_image/")

        context = {
            "form": form
        }

        return render(request, 'products_image/create.html', context)


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


def product_update_view(request, product_id):
    try:
        post = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return render(request, 'errors/404.html')

    if request.method == 'GET':
        context = {
            "form": ProductCreateForm2(instance=post)
        }
        return render(request, 'products/update.html', context)

    if request.method == 'PRODUCT':
        form = ProductCreateForm2(
            request.PRODUCT,
            request.FILES,
            instance=post
        )

        if form.is_valid():
            form.save()
            return redirect(f'/products/{product_id}/')

        return render(
            request,
            'products/update.html',
            {"form": form}
        )

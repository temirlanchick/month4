from django.shortcuts import HttpResponse, render


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
        return render(request, 'products/main.html')

from django.shortcuts import HttpResponse


def hello(request):
    if request.method == 'GET':
        return HttpResponse('Hello! Its my projects')


def current_date(request):
    if request.method == 'GET':
        return HttpResponse('14 november')


def goodbye(request):
    if request.method == 'GET':
        return HttpResponse('Goodbye user')

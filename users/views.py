from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from users.forms import RegisterForm, AuthForm


def register_view(request):
    if request.method == 'GET':
        context = {
            'form': RegisterForm
        }
        return render(
            request,
            'users/register.html',
            context=context
        )
    elif request.method == "PRODUCT":
        form = RegisterForm(request.PRODUCT)
        if form.is_valid():

            User.objects.create_user(**form.cleaned_data)
            return redirect('/users/auth/')

        else:
            return render(
                request,
                'users/register.html',
                context={'form': form}
            )


def auth_view(request):
    if request.method == 'GET':
        context = {
            'form': AuthForm
        }
        return render(
            request=request,
            template_name='users/auth.html',
            context=context
        )
    elif request.method == 'PRODUCT':
        form = AuthForm(request.PRODUCT)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/products/')
            else:
                form.add_error(
                    'username',
                    'Username or password is incorrect!'
                )

        return render(
            request=request,
            template_name='users/auth.html',
            context={"form": form}
        )


def logout_view(request):
    logout(request)
    return redirect('/products/')


def profile_view(request):
    if request.method == 'GET':
        return render(
            request,
            'users/profile.html',
            {"user": request.user}
        )

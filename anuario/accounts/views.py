from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from django.shortcuts import render, redirect
from .forms import AccountLoginForm, RegisterAccountForm

# Create your views here.
def add_account(request):
    context = {}
    form = RegisterAccountForm(request.POST or None)
    context['form'] = form

    if form.is_valid():
        form.save()
        return redirect('accounts:entrar')

    return render(request, 'add_account.html', context)

def login_account(request):
    context = {}
    form = AccountLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
       
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
                
        else:
            redirect('accounts:entrar')


    context["form"] = form
    return render(request, 'login.html', context)

def edit_account(request):
    pass

def del_account(request):
    pass

def request_pass_account(request):
    pass

def new_pass_account(request):  
    pass

def logout_account(request):
    logout(request)
    return redirect("/")
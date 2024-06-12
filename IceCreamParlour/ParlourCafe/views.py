from django.shortcuts import render, redirect
from .models import UserDb
from .UserForms import RegisterForm, LoginForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email_address']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password = password)
            if user:
                login(request, user)
                return render(request, 'index.html')


    else:
        form = LoginForm()
    return render(request, 'home.html', {'form': form})

def register(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            #content = UserForm.objects.get()
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html',{'form': form})

def homepage(request):
    return render(request, 'index.html')

def logout(request):
    logout(request)
    return redirect('home')

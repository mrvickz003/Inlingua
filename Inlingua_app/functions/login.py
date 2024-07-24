from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect


def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('dashboard')  # Change 'home' to the name of your desired redirect URL name
        else:
            messages.error(request, 'Invalid username or password.')
    context={
        'loginpage':False
    }
    return render(request, 'inlingua/login.html', context)  # Change 'login.html' to the name of your login template

def custom_logout(request):
    logout(request)
    return redirect('login') 
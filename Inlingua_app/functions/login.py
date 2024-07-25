from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.utils.http import url_has_allowed_host_and_scheme


def logout_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return view_func(request, *args, **kwargs)
    return _wrapped_view

@logout_required
def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            
            # Get the next parameter if it exists
            next_url = request.GET.get('next')
            if next_url and url_has_allowed_host_and_scheme(next_url, allowed_hosts=None):
                return redirect(next_url)
            else:
                return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    context={
        'loginpage':True
    }
    return render(request, 'inlingua/login.html', context)  # Change 'login.html' to the name of your login template

def custom_logout(request):
    logout(request)
    return redirect('login') 
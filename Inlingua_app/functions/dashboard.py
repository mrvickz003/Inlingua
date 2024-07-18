from django.shortcuts import render, redirect
from Inlingua_app.models import *

def dashboard(request):
    try:
        current_employee = employees.objects.get(user=request.user)
    except employees.DoesNotExist:
        current_employee = None

    context={
        'Dashboard':'active',
        'current_employee':current_employee,
    }
    return render(request, 'inlingua/dashboard.html',context)
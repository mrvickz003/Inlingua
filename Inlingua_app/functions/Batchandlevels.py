from django.shortcuts import render, redirect
from Inlingua_app.models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def batchandlanguage(request):
    try:
        current_employee = employees.objects.get(user=request.user)
    except employees.DoesNotExist:
        current_employee = None
    
    languages = Language.objects.all()
    levels = LevelsAndHour.objects.all()

    context={
        'courceandlevels':'active',
        'current_employee':current_employee,
        'languages':languages,
        'levels':levels,
        'languages':Language.objects.all()
    }
    return render(request, 'inlingua/Batchsandlevels.html',context)
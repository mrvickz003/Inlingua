import datetime as dt
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from Inlingua_app.models import *

def new_language(request):
    if request.method == 'POST':
        new_language = request.POST.get('language')
        if not Language.objects.filter(name=new_language).exists():
            language = Language.objects.create(
                name = new_language,
                created_by = request.user,
                created_date = dt.now()
                )
            language.save()
            messages.success(request, 'Language added successfully')
            return redirect('dashboard')
        else:
            messages.error(request, f'Language {new_language} already created')
            return redirect('dashboard')
    else:
        messages.success(request, 'Something went wrong')
        return redirect('dashboard')
    

def set_levelandhrs(request):
    if request.method == 'POST':
        language_id = request.POST.get('language')
        level = request.POST.get('level')
        hours = request.POST.get('hrs')
        
        try:
            language = Language.objects.get(pk=language_id)
        except Language.DoesNotExist:
            messages.error(request, 'Language does not exist')
            return redirect('dashboard')
        
        if LevelsAndHour.objects.filter(language=language, level=level).exists():
            messages.error(request, f'Level {level} for {language} already exists')
            return redirect('dashboard')
        
        new_setup = LevelsAndHour.objects.create(
            language=language,
            level=level,
            hours=hours,
            created_by=request.user,
            created_date=dt.now()
        )
        messages.success(request, f'Successfully set level and hours for {language}')
        return redirect('dashboard')
    else:
        messages.error(request, 'Invalid request method')
        return redirect('dashboard')
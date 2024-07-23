from django.shortcuts import render, redirect
from Inlingua_app.models import *
from django.core.paginator import Paginator
from django.db.models import Q

def create_batch(request):
    context={
        'Dashboard':'active',
        'languages':Language.objects.all(),
    }
    return render(request, 'inlingua/add_batchs.html', context)
from django.shortcuts import render, redirect
from Inlingua_app.models import *
from django.core.paginator import Paginator

def dashboard(request):
    try:
        current_employee = employees.objects.get(user=request.user)
    except employees.DoesNotExist:
        current_employee = None

    all_students = StudentTable.objects.filter(payment_complited=False)
    paginator = Paginator(all_students, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context={
        'Dashboard':'active',
        'current_employee':current_employee,
        'languages':Language.objects.all(),
        'all_students': page_obj,
        'page_obj': page_obj,
    }
    return render(request, 'inlingua/dashboard.html',context)
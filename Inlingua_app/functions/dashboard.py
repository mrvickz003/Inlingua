from django.shortcuts import render, redirect
from Inlingua_app.models import *
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def dashboard(request):
    try:
        current_employee = employees.objects.get(user=request.user)
    except employees.DoesNotExist:
        current_employee = None

    role_choices = employees.COURSE_CURRENT_ROLE

    all_students = StudentTable.objects.filter(Q(user__is_active=False) | Q(payment_complited=False))
    paginator = Paginator(all_students, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Trainer Head students list trainer_head_students_list_page_obj
    trainer_head_students_list = StudentTable.objects.filter(status='Verified')
    trainer_head_students_list_paginator = Paginator(trainer_head_students_list, 10)
    trainer_head_students_list_page_number = request.GET.get('page')
    trainer_head_students_list_page_obj = trainer_head_students_list_paginator.get_page(trainer_head_students_list_page_number)
    context={
        'Dashboard':'active',
        'current_employee':current_employee,
        'languages':Language.objects.all(),
        'all_students': page_obj,
        'page_obj': page_obj,
        'trainer_head_students_list_page_obj':trainer_head_students_list_page_obj,
        'role_choices': role_choices,
    }
    return render(request, 'inlingua/over_all_dashboard.html',context)
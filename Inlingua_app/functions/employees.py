from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from Inlingua_app.models import *
from django.http import JsonResponse
from django.core.paginator import Paginator
from Inlingua_app.utils import send_welcome_email

def employee_list(request):
    all_employees = employees.objects.all()[::-1]
    paginator = Paginator(all_employees, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'Employees':'active',
        'all_employees': page_obj, 
        'page_obj': page_obj,
    }
    return render(request, 'inlingua/employees.html', context)

def addemployee(request):
    if request.method == 'POST':
        employeename = request.POST.get('employeename')
        employeephonenumber =request.POST.get('employeephonenumber')
        employeemail = request.POST.get('employeemail')
        employeedob = request.POST.get('employeedob')
        employeedoj = request.POST.get('employeedoj')
        employeeaadharcard = request.FILES.get('employeeaadharcard')
        employeaddress = request.POST.get('employeaddress')
        Employeephoto = request.FILES.get('Employeephoto')

        isadmin = request.POST.get('isadmin')
        isbusinessmanager = request.POST.get('isbusinessmanager')
        trainerhead = request.POST.get('trainerhead')
        isaccountant = request.POST.get('isaccountant')
        businessdevelopment = request.POST.get('businessdevelopment')

        bankaccountnumber = request.POST.get('bankaccountnumber')
        bankname = request.POST.get('bankname')
        bankbranch = request.POST.get('bankbranch')
        bankifsccode = request.POST.get('bankifsccode')
        Passbookcopy = request.FILES.get('Passbookcopy')

    context = {
        'Employees': 'active'
    }    
    return render(request, "inlingua/addemployees.html", context)
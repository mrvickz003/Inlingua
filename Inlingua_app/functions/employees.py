from django.shortcuts import render, redirect
from django.contrib import messages
from Inlingua_app.models import *
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required(login_url='login')
def employee_list(request):
    try:
        current_employee = employees.objects.get(user=request.user)
    except employees.DoesNotExist:
        current_employee = None

    role_choices = employees.COURSE_CURRENT_ROLE

    all_employees = employees.objects.all().order_by('-id')  # or any other field for sorting
    paginator = Paginator(all_employees, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'Employees': 'active',
        'current_employee': current_employee,
        'all_employees': page_obj,
        'page_obj': page_obj,
        'role_choices': role_choices,
    }
    return render(request, 'inlingua/employees.html', context)

@login_required(login_url='login')
def addemployee(request):
    try:
        current_employee = employees.objects.get(user=request.user)
    except employees.DoesNotExist:
        current_employee = None

    role_choices = employees.COURSE_CURRENT_ROLE
    if request.method == 'POST':
        employeename = request.POST.get('employeename')
        employeephonenumber = request.POST.get('employeephonenumber')
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

        # Validation 
        if not Employeephoto:
            Employeephoto = None

        isadmin = True if isadmin == 'true' else False
        isbusinessmanager = True if isbusinessmanager == 'true' else False
        trainerhead = True if trainerhead == 'true' else False
        isaccountant = True if isaccountant == 'true' else False
        businessdevelopment = True if businessdevelopment == 'true' else False

        role_mapping = {
            'isadmin': 'Admin',
            'isbusinessmanager': 'Business Manager (BM)',
            'trainerhead': 'Trainer Head (TD)',
            'isaccountant': 'Accountant (AC)',
            'businessdevelopment': 'Business Development Executive (BDE)',
        }

        current_role = None
        for role, role_name in role_mapping.items():
            if locals()[role]:
                current_role = role_name
                break
        New_user = User.objects.create(
            email=employeemail,
        )
        New_employee = employees.objects.create(
            user=New_user,
            name=employeename,
            phone=employeephonenumber,
            email=employeemail,
            Date_of_birth=employeedob,
            employee_photo=Employeephoto,
            aadhar_card=employeeaadharcard,
            address=employeaddress,
            date_of_joining=employeedoj,
            bank_account_number=bankaccountnumber,
            bank_name=bankname,
            bank_branch=bankbranch,
            bank_ifsc=bankifsccode,
            passbook=Passbookcopy,
            is_admin=isadmin,
            is_business_manager=isbusinessmanager,
            is_trainer_head=trainerhead,
            is_accoountant=isaccountant,
            is_business_development_executive=businessdevelopment,
            current_role=current_role,
            Created_by=request.user,
            Created_date=timezone.now()
        )
        New_employee.save()
        New_user.username = New_employee.employee_ID
        New_user.set_password(employeemail)
        New_user.save()
        return redirect('employee_list')
    context = {
        'Employees': 'active',
        'current_employee':current_employee,
        'role_choices':role_choices,
    }    
    return render(request, "inlingua/addemployees.html", context)

@login_required(login_url='login')
def rolemaping(request, role):
    try:
        current_employee = employees.objects.get(user=request.user)
        current_employee.current_role = role
        current_employee.save()
        messages.success(request, f'Success fully role change in {role}')
        return redirect('dashboard')
    except employees.DoesNotExist:
        messages.error(request, f'Sorry this user is not a authendicate')
        return redirect('dashboard')

    
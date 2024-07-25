from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from Inlingua_app.models import *
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.urls import reverse
from Inlingua_app.utils import send_welcome_email
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def student_list(request):
    all_students = StudentTable.objects.all()[::-1]
    paginator = Paginator(all_students, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'Students':'active',
        'all_students': page_obj, 
        'page_obj': page_obj,
    }
    return render(request, 'inlingua/user.html', context)

@login_required(login_url='login')
def addstudent(request):
    if request.method == 'POST':
        student_name = request.POST.get('studentname')
        student_phone_no = request.POST.get('studentmobilenumber')
        student_mail_id = request.POST.get('email')
        student_date_of_birth = request.POST.get('studentdob')
        identity_card_aadhar_copy = request.FILES.get('studentaadharcard')
        Profession = request.POST.get('professions')
        student_photo = request.FILES.get('studentphoto')
        Batch_type = request.POST.get('batch_types')
        language_name_id = request.POST.get('language')
        level_and_hour_id = request.POST.get('level')
        course_type = request.POST.get('Course-type')
        student_counselor_id = request.POST.get('nameOfCounselor')
        payment_type = request.POST.get('Payment-type')
        transaction_id = request.POST.get('transactionid')
        account_holder_name = request.POST.get('account-holder-name')
        amount_paide = float(request.POST.get('Amount-paid'))
        balance_amount = float(request.POST.get('balanceamount'))

        language_name = Language.objects.get(id=language_name_id)
        level_and_hour = LevelsAndHour.objects.get(id=level_and_hour_id)
        student_counselor = NameOfCounselor.objects.get(id=student_counselor_id)
        course_type = batch_preferences.objects.get(pk=course_type)
        
        new_user = User.objects.create(
            username = student_mail_id,
            email = student_mail_id,
            is_active = False,
            is_staff = False,
            is_superuser = False,
        )
        new_user.set_password(student_mail_id)
        new_user.save()

        student = StudentTable.objects.create(
            user=new_user,
            Student_Name=student_name,
            Student_Phone_No=student_phone_no,
            Student_Mail_Id=student_mail_id,
            Student_Date_of_Birth=student_date_of_birth,
            Identity_Card_Aadhar_Copy=identity_card_aadhar_copy,
            Profession=Profession,
            Student_Photo=student_photo,
            Language_Name=language_name,
            Level_and_Hour=level_and_hour,
            batch_preferences=course_type,
            Student_Counselor=student_counselor,
            Batch_type=Batch_type,
            Payment_Type=payment_type,
            Transaction_ID=transaction_id,
            Account_Holder_Name=account_holder_name,
            Amount_Paide=amount_paide,
            Balance_Amount=balance_amount,
            status=StudentTable.STATUS_CHOICES[0][0],  # Using the constant
            Created_by=request.user,
            Created_date=dt.now(),
        )
        student.save()
        return redirect('student_list')

    context = {
        'Students': 'active',
        'All_languages': Language.objects.all(),
        'nameOfCounselor': NameOfCounselor.objects.all(),
        'Payment_Type': StudentTable.PAYMENT_TYPE_CHOICES,
        'professions': StudentTable.PROFESSION_CHOICES,
        'batch_types': StudentTable.BATCH_TYPE_CHOICES,
        'Batch_Preferences' : batch_preferences.objects.all()
    }    
    return render(request, "inlingua/addstudent.html", context)

@login_required(login_url='login')
def verify(request, pk):
    get_student = get_object_or_404(StudentTable, pk=pk)
    if not get_student.user.is_active:
        if request.method == 'POST':
            get_student.status = StudentTable.STATUS_CHOICES[1][0]
            get_student.updated_by = request.user
            get_student.Updated_date = dt.now()
            get_student.user.is_active = True
            get_student.save()
            get_student.user.save()
            send_welcome_email(get_student.user.email, get_student.Student_Name)
            messages.success(request, f'Student {get_student.Student_Name} success fully verified and activated ...')
            return redirect('dashboard')
        context={
            'Dashboard':'active',
            'get_student':get_student,
        }
        return render(request, "inlingua/students_details.html", context)
    else:
        messages.error(request, f'Student {get_student.Student_Name} is already verified and activated')
        return redirect('dashboard')

@login_required(login_url='login')
def get_levels(request, language_id):
    levels = LevelsAndHour.objects.filter(language=language_id).values('id','level', 'hours', )
    print(levels)
    return JsonResponse({'levels': list(levels)})

@login_required(login_url='login')
def full_payments(request, pk):
    if request.method == 'POST':
        get_student = get_object_or_404(StudentTable, pk=pk)
        get_student.payment_complited = True
        get_student.updated_by = request.user
        get_student.Updated_date = dt.now()
        get_student.save()
        messages.success(request, 'Payment Complited success fully updated')
        return redirect(reverse('verify', kwargs={'pk':pk}))

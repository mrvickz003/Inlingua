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
        student_name = request.POST.get('studentname')
        student_phone_no = request.POST.get('studentmobilenumber')
        student_mail_id = request.POST.get('email')
        student_date_of_birth = request.POST.get('studentdob')
        identity_card_aadhar_copy = request.FILES.get('studentaadharcard')
        student_photo = request.FILES.get('studentphoto')
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


        new_user = User.objects.create(
            username = student_mail_id,
            email = student_mail_id,
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
            Student_Photo=student_photo,
            Language_Name=language_name,
            Level_and_Hour=level_and_hour,
            Course_Type=course_type,
            Student_Counselor=student_counselor,
            Payment_Type=payment_type,
            Transaction_ID=transaction_id,
            Account_Holder_Name=account_holder_name,
            Amount_Paide=amount_paide,
            Balance_Amount=balance_amount,
            Created_by=request.user,
            Updated_by=request.user,
        )
        student.save()
        send_welcome_email(student.Student_Mail_Id, student.Student_Name)
        return redirect('student_list') 

    context = {
        'Employees': 'active',
        'All_languages': Language.objects.all(),
        'nameOfCounselor': NameOfCounselor.objects.all(),
        'Course_Type': StudentTable.COURSE_TYPE_CHOICES,
        'Payment_Type': StudentTable.PAYMENT_TYPE_CHOICES,
    }    
    return render(request, "inlingua/addemployees.html", context)
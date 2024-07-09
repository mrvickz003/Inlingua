from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from Inlingua_app.models import *
from django.http import JsonResponse
from django.core.paginator import Paginator

def user_page(request):
        context = {
                'Students':'active',
                'all_students': StudentTable.objects.all(),
                }
        return render(request, "inlingua/user.html",context)


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


# def student_details(request,id):
#     context = {
#         'Students':'active',
#     }
#     return render(request, "inlingua/student_details.html",context)

def addstudent(request):
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
            Created_by=request.user.username,
            Updated_by=request.user.username,
        )
        student.save()

        return redirect('students') 

    context = {
        'Students': 'active',
        'All_languages': Language.objects.all(),
        'nameOfCounselor': NameOfCounselor.objects.all(),
        'Course_Type': StudentTable.COURSE_TYPE_CHOICES,
        'Payment_Type': StudentTable.PAYMENT_TYPE_CHOICES,
    }    
    return render(request, "inlingua/addstudent.html", context)




def get_levels(request, language_id):
    levels = LevelsAndHour.objects.filter(language=language_id).values('id', 'level', 'hours', 'help_text')
    return JsonResponse({'levels': list(levels)})

# def profileupdate(request, id):
#     if request.user.is_authenticated:
#         user_id = request.user.id
#         user = User.objects.get(id=user_id)
#         if user.is_staff and user.is_staff and user.is_superuser:
#             if request.method == 'POST':
#                 profile = request.FILES.get('changeimg')
#                 if profile:
#                     changeprofile = User.objects.get(id = id)
#                     changeprofile.user_img =  profile
#                     changeprofile.save()
#                     messages.success(request,  f"Profile picture updated successfully!")
#                     return redirect('students')
#                 else:
#                     messages.error(request,  "Image field is empty! Please select an image to update your profile picture.")
#                     return redirect('students')
#             else:
#                 user_detail = get_object_or_404(User, id=id)
#                 context={'User':user,'Users':user_detail}
#                 return render(request,'inlingua/admin-editProfile.html',context)
#         else:
#             messages.error(request, "You are not authorized to view this page ")
#             return redirect('home')
#     else:
#         messages.info(request, "Please Login first!")
#         return redirect('login')  
                
# def basic_details_update(request, id):
#     if request.user.is_authenticated:
#         user_id = request.user.id
#         user = User.objects.get(id=user_id)
#         if user.is_staff and user.is_staff and user.is_superuser:
#             if request.method == 'POST':
#                 studentname = request.POST.get('studentname')
#                 mobilenumber = request.POST.get('mobilenumber')
#                 fname = request.POST.get('fname')
#                 lname = request.POST.get('lname')
#                 email = request.POST.get('email')
#                 Location = request.POST.get('Location')
                
#                 if studentname and mobilenumber and email and Location :
#                     getuser = User.objects.get(id = id)
#                     getuser.name = studentname
#                     getuser.Mobile_Number = mobilenumber
#                     getuser.first_name = fname
#                     getuser.last_name = lname
#                     getuser.Address =  Location
#                     if getuser.email ==  email:
#                         pass
#                     else:
#                         if not User.objects.filter(email=email).exists():
#                             getuser.email = email
#                             getuser.save()
#                         else:
#                             messages.warning(request,"Email already exists.")
#                             return redirect('students')
#                     getuser.save()
#                     messages.success(request,  f"{studentname} Basic information details updated successfully")
#                     return redirect('students')
#                 else:
#                     messages.error(request,  "All fields must be filled out correctly.")
#                     return redirect('students')
#             else:
#                 user_detail = get_object_or_404(User, id=id)
#                 context={'User':user,'Users':user_detail}
#                 return render(request,'inlingua/admin-editProfile.html',context)
#         else:
#             messages.error(request, "You are not authorized to view this page ")
#             return redirect('home')
#     else:
#         messages.info(request, "Please Login first!")
#         return redirect('login')  
    
# def studentbatchdetals(request, id):
#     if request.user.is_authenticated:
#         user_id = request.user.id
#         user = User.objects.get(id=user_id)
#         if user.is_staff and user.is_staff and user.is_superuser:
#             if request.method == 'POST':
#                 batch = request.POST['Batchid']
#                 try:
#                     getbatch = TrainingBatches.objects.get(ID = int(batch))
#                 except:
#                     messages.error(request, "Invalid Batch ID")
#                     return redirect('students')

#                 if getbatch:
#                     updatestudent = StudentDetails.objects.get(StudentID=id)
#                     updatestudent.BatchID = getbatch
#                     updatestudent.StudentID.updated_by =  user.name
#                     updatestudent.StudentID.updated_date =  datetime.datetime.now()
#                     updatestudent.save()
#                     messages.success(request,  f"Course details updated successfully")
#                     return redirect('students')
#                 else:
#                     messages.warning(request, 'Sorry Select a corrct Course')
#                     return redirect('students')
#             else:
#                 messages.error(request, "You are not authorized to view this page ")
#                 return redirect('home')
#         else:
#             messages.error(request, "You are not authorized to view this page ")
#             return redirect('home')
#     else:
#         messages.info(request, "Please Login first!")
#         return redirect('login')  
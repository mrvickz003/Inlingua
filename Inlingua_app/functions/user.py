from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from Inlingua_app.models import *
from django.http import JsonResponse

def user_page(request):
        context = {
                'Students':'active'
                }
        return render(request, "inlingua/user.html",context)

# def student_details(request,id):
#     context = {
#         'Students':'active',
#     }
#     return render(request, "inlingua/student_details.html",context)

def addstudent(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        lasttname = request.POST.get('lname')
        Email = request.POST.get('gmail')
        mobilenumber = request.POST.get('mobilenumber')
        studentphoto = request.FILES.get('studentphoto')
        password1 = Email
        Batchid = request.POST.get('Batchid')
        languageid = request.POST.get('languageid')
        studentid = request.POST.get('studentid')
        address = request.POST.get('Address')

    context = {
                'Students':'active',
                'All_languages' : language.objects.all(),
                'nameOfCounselor':nameOfCounselor.objects.all(),
                }    
    return render(request, "inlingua/addstudent.html",context)



def get_levels(request, language_id):
    levels = levelsandhour.objects.filter(Language_id=language_id).values('id', 'Level', 'Hours', 'Help_Text')
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
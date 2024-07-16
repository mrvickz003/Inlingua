import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from Inlingua_app.models import (User, Language, TrainerQualifications, LevelsAndHour, trainer_table)

def trainers_view(request):
        languages = Language.objects.all() 
        level = LevelsAndHour.objects.all()
        training_Staff = TrainerQualifications.objects.all()
        context = {
            'User': request.user,  
            'languages': languages,
            'training_Staff': training_Staff,
            'levels': level,
            'Trainers': 'active'
        }
        return render(request, "inlingua/trainers.html", context)
    
def add_trainer(request):
    if request.method == 'POST':
        # Retrieve all form fields
        trainer_name = request.POST.get('trainer_name')
        trainer_dob = request.POST.get('trainer_dob')
        trainer_education = request.POST.get('trainer_education')
        trainer_mail = request.POST.get('trainer_mail')
        trainer_phone = request.POST.get('trainer_phone')
        trainer_languages = request.POST.get('trainer_languages')
        trainer_address = request.POST.get('trainer_address')
        trainer_photo = request.FILES.get('trainer_photo')  # Use request.FILES for file fields
        trainer_bank_details = request.POST.get('trainer_bank')
        trainer_aadhar = request.POST.get('trainer_aadhar')
        trainer_role = request.POST.get('trainer_role')

        # Example: Create a Trainer object and save it to the database
        new_trainer = trainer_table.objects.create(
            name=trainer_name,
            dob=trainer_dob,
            education=trainer_education,
            mail=trainer_mail,
            phone=trainer_phone,
            languages=trainer_languages,
            address=trainer_address,
            photo=trainer_photo,
            bank_details=trainer_bank_details,
            aadhar=trainer_aadhar,
            role=trainer_role
        )
        new_trainer.save()

# def add_trainer_head(request, id):
#     if request.user.is_authenticated:
#         user = request.user

#         if user.is_staff and user.is_superuser:
#             try:
#                 trainer_qualification = TrainerQualifications.objects.get(ID=id)
#                 training_batches = TrainingBatches.objects.filter(TrainerId = trainer_qualification.TrainerId)

#                 if not training_batches:
#                     if TrainerQualifications.objects.filter(LanguageID=trainer_qualification.LanguageID, TrainerHead=True).exists():
#                         messages.error(request, 'Already a Head Coach!')
#                         return redirect('trainers')
#                     else:
#                         trainer_qualification.TrainerHead = True
#                         trainer_qualification.TrainerId.LoginId.is_staff_head = True
#                         trainer_qualification.TrainerId.LoginId.save()
#                         trainer_qualification.save()

#                         messages.success(request, 'Successfully made the Trainer as a Head Coach!')
#                         return redirect('trainers')
#                 else:
#                     messages.error(request, 'This trainer has a batch, so if you add this trainer to the head trainer, remove the batch and add the trainer.')
#                     return redirect('trainers')
#             except TrainerQualifications.DoesNotExist:
#                 messages.error(request, 'Trainer qualifications not found.')
#                 return redirect('trainers')
#         else:
#             messages.error(request, "You don't have permission for that action.")
#             return redirect('home')
#     else:
#         messages.error(request, "Please log in first.")
#         return redirect('login')
    
    

# def remove_trainer_head(request,id):
#     get_tainer_qualification = TrainerQualifications.objects.get(ID = id)
#     get_tainer_qualification.TrainerHead = False
#     get_tainer_qualification_loginid = User.objects.get(pk = get_tainer_qualification.TrainerId.LoginId.pk)
#     get_tainer_qualification_loginid.is_staff_head = False
#     get_tainer_qualification.save()
#     get_tainer_qualification_loginid.save()
#     return redirect('trainers')
def add_trainers(request):
                # try:
                #     lastuser = User.objects.last()
                #     new_trainer_details = TrainingStaff.objects.create(
                #         Name = name,
                #         EmailID = email,
                #         LoginId = lastuser,
                #         IsActive = True,
                #         CreatedBy = user.name,
                #         CreatedDate = datetime.datetime.now(),
                #         UpdatedBy = user.name,
                #         UpdatedDate = datetime.datetime.now(),
                #     )
                #     new_trainer_details.save()
                #     Language = Languages.objects.get(ID = int(language))
                #     level = Level.objects.get(ID = int(level))
                #     lastuser = TrainingStaff.objects.last()
                    
                #     new_trainer_qualification = TrainerQualifications.objects.create(
                #         userid = trainerid,
                #         LanguageID = Language,
                #         LevelId = level,
                #         CertificateNumber = certificateNumber,
                #         CertifyingAuthority = certifyingAuthority,
                #         CertificateValidTill = certificateValidTill,
                #         TrainerId = lastuser,
                #         CreatedBy = user.name,
                #         CreatedDate = datetime.datetime.now(),
                #         UpdatedBy = user.name,
                #         UpdatedDate = datetime.datetime.now(),
                #     )
                #     new_trainer_qualification.save()
                # except Exception as e:
                #     messages.error(request, f"{e}")
                #     return redirect('trainers')

            context = {'Trainers':'active'}
            return render(request, 'inlingua/addtrainer.html', context)
    
# def trainerprofileupdate(request, id):
#     if request.user.is_authenticated:
#         user_id = request.user.id
#         user = User.objects.get(id=user_id)
#         if user.is_staff and user.is_staff and user.is_superuser:
#             if request.method == 'POST':
#                 profile = request.FILES.get('trainerprofile')
#                 if profile:
#                     changeprofile = User.objects.get(id = id)
#                     changeprofile.user_img =  profile
#                     changeprofile.save()
#                     messages.success(request,  f"Profile picture updated successfully!")
#                     return redirect('trainers')
#                 else:
#                     messages.error(request,  "Image field is empty! Please select an image to update your profile picture.")
#                     return redirect('trainers')
#             else:
#                 messages.error(request,  "No file selected.")
#                 return redirect('trainers')
#         else:
#             messages.error(request, "You are not authorized to view this page ")
#             return redirect('home')
#     else:
#         messages.info(request, "Please Login first!")
#         return redirect('login')  
    
# def trainerbasicdetailsupdate(request,id):
#     if request.user.is_authenticated:
#         user_id = request.user.id
#         user = User.objects.get(id=user_id)
#         if user.is_staff and user.is_staff and user.is_superuser:
#             if request.method == 'POST':
#                 trainername = request.POST.get('trainername')
#                 mobilenumber = request.POST.get('mobilenumber')
#                 email = request.POST.get('email')
#                 Location = request.POST.get('location')
                
#                 if trainername and mobilenumber and email and Location :
#                     getuser = User.objects.get(id = id)
#                     getuser.name = trainername
#                     getuser.Mobile_Number = mobilenumber
#                     getuser.Address =  Location
#                     if getuser.email ==  email:
#                         pass
#                     else:
#                         if not User.objects.filter(email=email).exists():
#                             getuser.email = email
#                             getuser.save()
#                         else:
#                             messages.warning(request,"Email already exists.")
#                             return redirect('trainers')
#                     getuser.save()
#                     messages.success(request,  f"{trainername} Basic information details updated successfully")
#                     return redirect('trainers')
#                 else:
#                     messages.error(request,  "All fields must be filled out correctly.")
#                     return redirect('trainers')
#             else:
#                 messages.error(request,  "Invalid Request")
#                 return redirect('trainers')
#         else:
#             messages.error(request, "You are not authorized to view this page ")
#             return redirect('home')
#     else:
#         messages.info(request, "Please Login first!")
#         return redirect('login')  
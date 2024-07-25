import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from Inlingua_app.models import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def trainers_view(request):
    trainersList = TrainerTable.objects.all()
    paginatorTrainer = Paginator(trainersList, 10)
    pageNumber = request.GET.get('page')
    pageObjTrainer = paginatorTrainer.get_page(pageNumber)
    context = {
        'Trainers': 'active',
        'trainersList': TrainerTable.objects.all(),
        'paginator': pageObjTrainer,
        'PageObjTrainer': pageObjTrainer
    }
    return render(request, "inlingua/trainers.html", context)

@login_required(login_url='login')
def add_trainers(request):
    if request.method == 'POST':
        # Step 1: Trainer Personal Details
        trainer_name = request.POST.get('trainer_name')
        trainer_dob = request.POST.get('trainer_dob')
        trainer_mail = request.POST.get('trainer_mail')
        trainer_phone = request.POST.get('trainer_phone')
        trainer_address = request.POST.get('trainer_address')
        trainer_aadhar = request.FILES.get('trainer_aadhar')  # Use request.FILES for file fields
        trainer_photo = request.FILES.get('trainer_photo')  # Use request.FILES for file fields

        # Retrieve or create the language instance based on form input
        trainer_languages = request.POST.get('trainer_languages')
        trainer_language = Language.objects.get(id=trainer_languages)

        # Step 2: Education Details
        qualification = request.POST.get('education_qualification')
        institute = request.POST.get('education_institute')
        year_of_passing = request.POST.get('education_year_of_passing')

        # Step 3: Bank Details
        account_number = request.POST.get('bank_account_number')
        bank_name = request.POST.get('bank_name')
        branch = request.POST.get('bank_branch')
        ifsc_code = request.POST.get('bank_ifsc_code')
        passbook_front_page = request.FILES.get('bank_passbook')

        # Create User table
        New_user = User.objects.create(
            email=trainer_mail,   
        )
        
        # Create a new Trainer object and save it to the database

        new_trainer = TrainerTable.objects.create(
            user = New_user,
            trainer_name=trainer_name,
            trainer_dob=trainer_dob,
            trainer_mail=trainer_mail,
            trainer_phone=trainer_phone,
            trainer_languages=trainer_language,
            trainer_address=trainer_address,
            trainer_aadhar = trainer_aadhar,
            trainer_photo=trainer_photo,
            qualification=qualification,
            institution=institute,
            year_of_passing=year_of_passing,
            bank_account_number=account_number,
            bank_name=bank_name,
            bank_branch=branch,
            bank_ifsc=ifsc_code,
            passbook=passbook_front_page,
            
            Created_by=request.user,
            Created_date=dt.now()
        )
        New_user.username = new_trainer.Trainer_ID
        New_user.set_password(trainer_mail)
        New_user.save()
        new_trainer.save()
        return redirect('trainers')
    
    context = {
        'All_languages': Language.objects.all()
        }
    return render(request, "inlingua/addtrainer.html", context)



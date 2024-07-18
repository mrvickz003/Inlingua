import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.paginator import Paginator
from Inlingua_app.models import (User, Language, TrainerQualifications, LevelsAndHour, trainer_table)

def trainers_view(request):
    trainersList = trainer_table.objects.all()
    paginatorTrainer = Paginator(trainersList, 10)
    pageNumber = request.GET.get('page')
    pageObj = paginatorTrainer.get_page(pageNumber)
    context = {
        'Trainers': 'active',
        'trainersList': trainer_table.objects.all(),
        'paginatorTrainer': pageObj,
        'PageObj': pageObj
    }
    return render(request, "inlingua/trainers.html", context)

def add_trainers(request):
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
            trainer_name_mod = trainer_name,
            trainer_dob_mod = trainer_dob,
            trainer_education_mod = trainer_education,
            trainer_mail_mod = trainer_mail,
            trainer_phone_mod = trainer_phone,
            trainer_languages_mod = trainer_languages,
            trainer_address_mod = trainer_address,
            trainer_photo_mod = trainer_photo,
            trainer_bank_details_mod = trainer_bank_details,
            trainer_aadhar_mod = trainer_aadhar,
            trainer_role_mod = trainer_role
        )
        new_trainer.save()
    return render(request, 'inlingua/addtrainer.html')





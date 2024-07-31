from django.shortcuts import render, redirect
from django.urls import reverse
from Inlingua_app.models import *
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib import messages

@login_required(login_url='login')
def all_batches(request):
    try:
        current_employee = employees.objects.get(user=request.user)
    except employees.DoesNotExist:
        current_employee = None

    role_choices = employees.COURSE_CURRENT_ROLE

    batches = Batch.objects.all()[::-1]
    paginator = Paginator(batches, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={
        'all_batches':'active',
        'page_obj': page_obj,
        'current_employee': current_employee,
        'role_choices': role_choices,
    }
    return render(request, 'inlingua/all_batches.html', context)

@login_required(login_url='login')
def open_batch(request,bpk):
    try:
        current_employee = employees.objects.get(user=request.user)
    except employees.DoesNotExist:
        current_employee = None
    role_choices = employees.COURSE_CURRENT_ROLE
    get_batch = Batch.objects.get(pk=bpk)
    trainers = TrainerTable.objects.filter(
        Q(trainer_languages=get_batch.language) & 
        Q(user__is_active=True)
    )
    students = StudentTable.objects.filter(
        Q(Language_Name=get_batch.language) & 
        Q(Level_and_Hour=get_batch.levels) & 
        Q(batch_preferences=get_batch.batch_preferences) & 
        Q(Batch_type=BatchType.objects.get(type='Group')) & 
        Q(status=StudentTable.STATUS_CHOICES[1][0])
    )
    context={
        'all_batches':'active',
        'current_employee': current_employee,
        'role_choices': role_choices,
        'get_batch':get_batch,
        'trainers':trainers,
        'students':students,
    }
    return render(request, 'inlingua/open_batch.html', context)

@login_required(login_url='login')
def create_batch(request):
    try:
        current_employee = employees.objects.get(user=request.user)
    except employees.DoesNotExist:
        current_employee = None

    role_choices = employees.COURSE_CURRENT_ROLE

    if request.method == 'POST':
        batch_language_id = request.POST.get('batch_language')
        language_level_id = request.POST.get('language_level')
        batch_preference_id = request.POST.get('batch_preference')
        time_slot_id = request.POST.get('time_slot')
        startdate = request.POST.get('startdate')
        enddate = request.POST.get('enddate')
        student_ids = request.POST.getlist('students')

        # Fetch the related instances from the database
        batch_language = Language.objects.get(id=batch_language_id)
        language_level = LevelsAndHour.objects.get(id=language_level_id)
        batch_preference = batch_preferences.objects.get(id=batch_preference_id)
        time_slot = BatchTiming.objects.get(id=time_slot_id)
        students = StudentTable.objects.filter(id__in=student_ids)

        # Create the new batch
        batch = Batch.objects.create(
            batch_name=f'{batch_language.name}-{language_level.level}-{batch_preference.batch_preferences}-{datetime.strptime(startdate, "%Y-%m-%d").strftime("%d-%b-%Y")}',
            language=batch_language,
            levels=language_level,
            batch_preferences=batch_preference,
            time_slot=time_slot,
            course_start_date = startdate,
            course_End_date = enddate,
            Created_by=request.user,
            Created_date=dt.now()
        )
        batch.students.set(students)
        for student in students:
            student.status=StudentTable.STATUS_CHOICES[2][0]
            student.save()
        return redirect('all_batches')

    # If not POST, render a form (assuming you have a form template
    context={
        'all_batches':'active',
        'languages':Language.objects.all(),
        'batchtypes':BatchType.objects.all(),
        'Batch_Preferences':batch_preferences.objects.all(),
        'Batch_type': None,
        'current_employee':current_employee,
        'role_choices':role_choices,
    }
    return render(request, 'inlingua/add_batchs.html', context)

@login_required(login_url='login')
def load_levels(request):
    language_id = request.GET.get('language_id')
    levels = LevelsAndHour.objects.filter(language_id=language_id).values('id', 'level')
    return JsonResponse(list(levels), safe=False)

@login_required(login_url='login')
def load_time_slots(request):
    batchpreference_id = request.GET.get('batchpreference_id')
    time_slots = BatchTiming.objects.filter(batch_preferences=batchpreference_id).values('id', 'timing')
    return JsonResponse(list(time_slots), safe=False)

@login_required(login_url='login')
def get_students(request):
    batchpreference_id = request.GET.get('batchpreference')
    language_id = request.GET.get('language')
    level_id = request.GET.get('level')
    batchtype_id = request.GET.get('batchtypes')

    # Get values in table
    batchpreference_id = batch_preferences.objects.get(pk=batchpreference_id)
    language_id = Language.objects.get(pk=language_id)
    level_id = LevelsAndHour.objects.get(pk=level_id)
    batchtype_id = BatchType.objects.get(pk=batchtype_id)

    # Query the StudentTable to get the students based on the provided filters
    all_students = StudentTable.objects.filter(
        Language_Name=language_id,
        Level_and_Hour=level_id,
        batch_preferences=batchpreference_id,
        Batch_type = batchtype_id,
        status = StudentTable.STATUS_CHOICES[1][0]
    ).values('pk', 'Student_ID', 'Student_Name')
    
    # Convert the QuerySet to a list and return it as JSON response
    return JsonResponse(list(all_students), safe=False)

# Update batch tetails

@login_required(login_url='login')
def batch_meeturl(request,bpk):
    if request.method == 'POST':
        batch = Batch.objects.get(pk=bpk)
        batch.class_url = request.POST.get('gmeetlink')
        batch.Updated_by = request.user
        batch.Updated_date = timezone.now()
        batch.save()
        messages.success(request, 'Class link updated successfully ...')
    else:
        messages.error(request, 'Failed to update class link ...')
    return redirect(reverse('open_batch', kwargs={'bpk': bpk}))

@login_required(login_url='login')
def add_batch_trainer(request,bpk, tpk):
    if request.method == 'POST':
        batch = Batch.objects.get(pk=bpk)
        trainer = TrainerTable.objects.get(pk=tpk)
        batch.trainer= trainer
        batch.Updated_by = request.user
        batch.Updated_date = timezone.now()
        batch.save()
        messages.success(request, 'Class Trainer updated successfully ...')
    else:
        messages.error(request, 'Failed to update class Trainer ...')
    return redirect(reverse('open_batch', kwargs={'bpk': bpk}))

@login_required(login_url='login')
def add_batch_student(request,bpk, spk):
    if request.method == 'POST':
        batch = Batch.objects.get(pk=bpk)
        student = StudentTable.objects.get(pk=spk)
        batch.students.add(student)
        batch.Updated_by = request.user
        batch.Updated_date = timezone.now()
        batch.save()
        student.status=StudentTable.STATUS_CHOICES[2][0]
        student.save()
        messages.success(request, 'Class Student updated successfully ...')
    else:
        messages.error(request, 'Failed to update class Student ...')
    return redirect(reverse('open_batch', kwargs={'bpk': bpk}))

from django.shortcuts import render, redirect
from Inlingua_app.models import *
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse

def create_batch(request):
    if request.method == 'POST':
        batch_language_id = request.POST.get('batch_language')
        language_level_id = request.POST.get('language_level')
        batch_preference_id = request.POST.get('batch_preference')
        time_slot_id = request.POST.get('time_slot')
        student_ids = request.POST.getlist('students')

        # Fetch the related instances from the database
        batch_language = Language.objects.get(id=batch_language_id)
        language_level = LevelsAndHour.objects.get(id=language_level_id)
        batch_preference = batch_preferences.objects.get(id=batch_preference_id)
        time_slot = BatchTiming.objects.get(id=time_slot_id)
        students = StudentTable.objects.filter(id__in=student_ids)

        # Create the new batch
        batch = Batch.objects.create(
            batch_name=f'{batch_language.name}-{language_level.level}-{batch_preference.batch_preferences}-{dt.now().date()}',
            language=batch_language,
            levels=language_level,
            batch_preferences=batch_preference,
            time_slot=time_slot,
            Created_by=request.user,
            Created_date=dt.now()
        )

        # Add students to the batch
        batch.students.set(students)

        return redirect('dashboard')

    # If not POST, render a form (assuming you have a form template
    context={
        'Dashboard':'active',
        'languages':Language.objects.all(),
        'Batch_Preferences':batch_preferences.objects.all()
    }
    return render(request, 'inlingua/add_batchs.html', context)


def load_levels(request):
    language_id = request.GET.get('language_id')
    levels = LevelsAndHour.objects.filter(language_id=language_id).values('id', 'level')
    return JsonResponse(list(levels), safe=False)

def load_time_slots(request):
    batchpreference_id = request.GET.get('batchpreference_id')
    time_slots = BatchTiming.objects.filter(batch_preferences=batchpreference_id).values('id', 'timing')
    return JsonResponse(list(time_slots), safe=False)

def get_students(request):
    batchpreference_id = request.GET.get('batchpreference')
    language_id = request.GET.get('language')
    level_id = request.GET.get('level')

    # Get values in table
    batchpreference_id = batch_preferences.objects.get(pk=batchpreference_id)
    language_id = Language.objects.get(pk=language_id)
    level_id = LevelsAndHour.objects.get(pk=level_id)

    # Query the StudentTable to get the students based on the provided filters
    all_students = StudentTable.objects.filter(
        Language_Name=language_id,
        Level_and_Hour=level_id,
        batch_preferences=batchpreference_id
    ).values('pk', 'Student_ID', 'Student_Name')
    
    # Convert the QuerySet to a list and return it as JSON response
    return JsonResponse(list(all_students), safe=False)
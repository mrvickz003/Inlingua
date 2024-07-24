from django.shortcuts import render, redirect
from Inlingua_app.models import *
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse

def create_batch(request):
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
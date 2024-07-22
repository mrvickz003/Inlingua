# admin.py
from django.contrib import admin
from Inlingua_app.models import *

admin.site.register(Language)
admin.site.register(LevelsAndHour)
admin.site.register(NameOfCounselor)
admin.site.register(StudentTable)
admin.site.register(TrainerTable)
admin.site.register(employees)
admin.site.register(batch_preferences)
admin.site.register(BatchTiming)
admin.site.register(Batch)
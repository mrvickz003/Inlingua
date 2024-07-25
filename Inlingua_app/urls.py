from django.urls import path
from Inlingua_app.functions import (
dashboard,
login,
user,
trainers, 
employees,
languages,
Batchandlevels,
batches,
)
from django.contrib.auth import views as password_views
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('login/', login.custom_login, name="login"), 
    path('logout/', login.custom_logout, name="custom_logout"),
        
    path('', dashboard.dashboard, name='dashboard'),
    path('employees/', employees.employee_list, name='employee_list'),
    path('employees/add/', employees.addemployee, name="addemployee"),
    
    # Trainer
    path('trainers/', trainers.trainers_view, name="trainers"),
    path('trainers/addtrainers/', trainers.add_trainers, name="addtrainers"),

    # Languages and levels
    path('batchandlanguage/', Batchandlevels.batchandlanguage, name="batchandlanguage"),
    path('new_language/', languages.new_language, name="new_language"),
    path('set_levelandhrs/', languages.set_levelandhrs, name="setlevelandhrs"),
    path('get_levels/<int:language_id>/', user.get_levels, name='get_levels'),

    # Students
    path('students/', user.student_list, name='student_list'),
    path('students/add/', user.addstudent, name="addstudent"),
    path('students/<int:pk>/verify/', user.verify, name="verify"),
    path('students/<int:pk>/full_payments_complited/', user.full_payments, name="full_payments"),

    # Batch Createtion
    path('batchs/', batches.all_batches, name="all_batches"),
    path('batch/create/', batches.create_batch, name="create_batch"),
    path('ajax/load-levels/', batches.load_levels, name='ajax_load_levels'),
    path('ajax/load-time-slots/', batches.load_time_slots, name='ajax_load_time_slots'),
    path('ajax/get_students/', batches.get_students, name='get_students'),

    # Role maping
    path('rolemaping/<str:role>', employees.rolemaping, name="rolemaping"),

    path('user/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('user/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('user/password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('user/password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('user/reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('user/reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.conf.urls import handler404
from Inlingua_app.functions.errors import custom_page_not_found_view

handler404 = custom_page_not_found_view
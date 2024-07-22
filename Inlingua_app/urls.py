from django.urls import path
from Inlingua_app.functions import (
dashboard,
login,
user,
trainers, 
employees,
languages,
Batchandlevels,
)
from django.contrib.auth import views as password_views
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('login/', login.custom_login, name="login"),
    
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


    # Role maping
    path('rolemaping/<str:role>', employees.rolemaping, name="rolemaping"),

    path('user/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('user/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('user/password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('user/password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('user/reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('user/reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from Inlingua_app.functions import (
login,
user,
trainers, 
employees
)
from django.contrib.auth import views as password_views
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('login/', login.custom_login, name="login"),

    path('students/', user.student_list, name='student_list'),
    path('mail/', user.mail, name='mail'),
    path('employees/', employees.employee_list, name='employee_list'),
    path('employees/add/', employees.addemployee, name="addemployee"),
    path('students/add/', user.addstudent, name="addstudent"),
    path('get_levels/<int:language_id>/', user.get_levels, name='get_levels'),

    path('trainers/', trainers.trainers_view, name="trainers"),
    path('trainers/addtrainers/', trainers.add_trainers, name="addtrainers"),

    path('user/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('user/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('user/password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('user/password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('user/reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('user/reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
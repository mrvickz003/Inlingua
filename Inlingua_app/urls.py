from django.urls import path
from Inlingua_app.functions import (
login, 
home, 
register, 
logout, 
batchdetails, 
user, 
tables, 
language as lng, 
trainers, 
language_page, 
courceandlevels,
payment, 
Generate_Report,
trainer_head,
StartClass,
Message_page,
)
from django.contrib.auth import views as password_views
from django.contrib.auth import views as auth_views
from .views import CustomPasswordResetView, CustomPasswordResetDoneView, CustomPasswordResetConfirmView, CustomPasswordResetCompleteView

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('login/', login.custom_login, name="login"),
    # path('logout/', logout.custom_logout, name="logout"),
    # path('', home.home, name="home"),

    # path('start_class/<int:id>/<int:classid>/', StartClass.classstart, name="start_class"),
    # path('end_class/<int:id>/<int:classid>/', StartClass.classend, name="endclass"),

    # path('home/students_online_status/', trainer_head.students, name="student_online"),
    # path('home/Batchlist/',  trainer_head.Batchlist, name="Batchlist"),

    path('students/', user.student_list, name='student_list'),
    path('students/', user.user_page, name="students"), 
    path('students/add/', user.addstudent, name="addstudent"),
    path('get_levels/<int:language_id>/', user.get_levels, name='get_levels'),
    # path('student/<int:id>/', user.student_details, name="studentdetails"),
    # path('student/profileupdate/<int:id>/', user.profileupdate, name="profileupdate"),
    # path('student/studentbatchdetals/<int:id>/', user.studentbatchdetals, name="studentbatchdetals"),
    # path('student/basic_details_update/<int:id>/', user.basic_details_update, name="basicdetailsupdate"),

    # path('students/payment/<int:id>/', payment.payment_view, name='payment'),
    # path('students/payment/history/<int:id>/', payment.history_view, name='history'),
    # path('students/payment/history/report/<int:id>/', Generate_Report.GenerateReport, name='generatereport'),

    # path('trainers/', trainers.trainers_view, name="trainers"),
    # path('trainers/addtrainers/', trainers.add_trainers, name="addtrainers"),
    # path('trainers/<int:id>/', trainers.trainer_view, name="trainer"),
    # path('student/trainerprofile/<int:id>/', trainers.trainerprofileupdate, name="trainerprofile"),
    # path('student/trainerbasicdetails/<int:id>/', trainers.trainerbasicdetailsupdate, name="trainerbasicdetails"),
    # path('trainers/addhead/<int:id>/', trainers.add_trainer_head, name="addhead"),
    # path('trainers/removehead/<int:id>/', trainers.remove_trainer_head, name="removehead"),

    # path('tables/', tables.table_page, name="tables"),
    # path('tables/addlanguage/', lng.language_view, name="language"),
    # path('tables/addlanguage/add/', lng.add_language, name="add_language"),
    # path('tables/language/<int:id>/', lng.edit_lang, name="edit_lang"),

    # path('courceandlevels_table/', courceandlevels.table_page, name="courceandlevels_table"),
    # path('courceandlevels_table/batchs/<int:id>/', courceandlevels.edit_batchs, name="edit_batchs"),
    # path('courceandlevels_table/cources/<int:id>/', courceandlevels.edit_cources, name="edit_cources"),
    # path('courceandlevels_table/level/<int:id>/', courceandlevels.edit_level, name="edit_level"),

    # path('courceandlevels_table/add_level/', courceandlevels.add_level, name="add_level"),
    # path('courceandlevels_table/add_course/', courceandlevels.add_course, name="add_course"),
    # path('courceandlevels_table/add_batchs/', courceandlevels.add_batchs, name="add_batchs"),

    # path('language/<str:name>/', language_page.language_view, name="language_view"),

    # path('batch/<int:id>/', batchdetails.batches, name="batches"),
    # path('user/register/', register.register, name="register"),

    # path('user/message/', Message_page.message_view, name="Message_page"),
    # path('user/message/<str:username>/', Message_page.Message_for_user, name="Message_for_user"),

    # Reset the password urls

    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
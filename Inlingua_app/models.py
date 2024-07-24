from datetime import datetime as dt
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_migrate
from django.dispatch import receiver

def Employee_data(instance, filename):
    Year = dt.now().year
    return f'Employee/{Year}/{instance.employee_ID}/{filename}'

def generate_employee_id():
    Year = str(dt.now().year)
    last_employee = employees.objects.order_by('-id').first()
    year = Year[2:]
    if last_employee and last_employee.Created_date.year == dt.now().year:
        last_id = int(last_employee.employee_ID[9:])
        new_id = last_id + 1
    else:
        new_id = 1
    return f'INL{year}EMP{new_id:04d}'

def Students_data(instance, filename):
    Year = dt.now().year
    return f'Students/{Year}/{instance.Student_ID}/{filename}'

def generate_customer_id():
    Year = str(dt.now().year)
    last_student = StudentTable.objects.order_by('-id').first()
    year = Year[2:]
    if last_student and last_student.Created_date.year == dt.now().year:
        last_id = int(last_student.Student_ID[7:])
        new_id = last_id + 1
    else:
        new_id = 1
    return f'INL{year}STD{new_id:04d}'

def generate_batch_id():
    Year = str(dt.now().year)
    last_trainer = TrainerTable.objects.order_by('-id').first()
    year = Year[2:]
    if last_trainer and last_trainer.Created_date.year == dt.now().year:
        last_id = int(last_trainer.Trainer_ID[7:])
        new_id = last_id + 1
    else:
        new_id = 1
    return f'INL{year}TR{new_id:04d}'

class batch_preferences(models.Model):
    batch_preferences = models.CharField(max_length=20)

    def __str__(self):
        return self.batch_preferences

class employees(models.Model):
    isadmin = 'isadmin'
    isbusinessmanager = 'isbusinessmanager'
    trainerhead = 'rainerhead'
    isaccountant = 'isaccountant'
    businessdevelopment = 'businessdevelopment'
    COURSE_CURRENT_ROLE = [
        (isadmin, 'Admin'),
        (isbusinessmanager, 'Business Manager (BM)'),
        (trainerhead, 'Trainer Head (TD)'),
        (isaccountant, 'Accountant (AC)'),
        (businessdevelopment, 'Business Development Executive (BDE)'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_employees')
    employee_ID = models.CharField(unique=True, default=generate_employee_id, null=False, blank=False, max_length=20)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    Date_of_birth = models.DateField(null=True, blank=True)
    employee_photo = models.FileField(upload_to=Employee_data, null=True, blank=True)
    aadhar_card = models.FileField(upload_to=Employee_data, null=True, blank=True)
    address = models.TextField(max_length=100)
    date_of_joining = models.DateField()

    #Bank Details
    bank_account_number = models.IntegerField()
    bank_name = models.CharField(max_length=100)
    bank_branch = models.CharField(max_length=100)
    bank_ifsc = models.CharField(max_length=11)
    passbook = models.FileField(upload_to=Employee_data, null=True, blank=True)

    # Roles
    is_admin = models.BooleanField(default=False)
    is_business_manager = models.BooleanField(default=False)
    is_trainer_head = models.BooleanField(default=False)
    is_accoountant = models.BooleanField(default=False)
    is_business_development_executive = models.BooleanField(default=False)
    current_role = models.CharField(choices=COURSE_CURRENT_ROLE, max_length=40)

    Created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employees_created_by')
    Created_date = models.DateTimeField()
    Updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='employees_updated_by')
    Updated_date = models.DateTimeField(null=True, blank=True,)

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class LevelsAndHour(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    level = models.CharField(max_length=5)
    hours = models.IntegerField()

    def __str__(self):
        return f" {self.level}"

@receiver(post_migrate)
def create_level_hour(sender, **kwargs):
    if sender.name == 'Inlingua_app':
        German, _ = Language.objects.get_or_create(name='German')
        LevelsAndHour.objects.get_or_create(language=German, level='A1', hours='60')
        LevelsAndHour.objects.get_or_create(language=German, level='A1.1', hours='30')
        LevelsAndHour.objects.get_or_create(language=German, level='A2', hours='60')
        LevelsAndHour.objects.get_or_create(language=German, level='B1', hours='90')
        LevelsAndHour.objects.get_or_create(language=German, level='B2', hours='100')
        LevelsAndHour.objects.get_or_create(language=German, level='C1', hours='120')
        LevelsAndHour.objects.get_or_create(language=German, level='C2', hours='150')

        French, _=Language.objects.get_or_create(name='French')
        LevelsAndHour.objects.get_or_create(language=French, level='A1', hours='60')
        LevelsAndHour.objects.get_or_create(language=French, level='A1.1', hours='30')
        LevelsAndHour.objects.get_or_create(language=French, level='A2', hours='60')
        LevelsAndHour.objects.get_or_create(language=French, level='B1', hours='90')
        LevelsAndHour.objects.get_or_create(language=French, level='B2', hours='100')
        LevelsAndHour.objects.get_or_create(language=French, level='C1', hours='120')
        LevelsAndHour.objects.get_or_create(language=French, level='C2', hours='150')

        Spanish, _=Language.objects.get_or_create(name='Spanish')
        LevelsAndHour.objects.get_or_create(language=Spanish, level='A1', hours='60')
        LevelsAndHour.objects.get_or_create(language=Spanish, level='A1.1', hours='30')
        LevelsAndHour.objects.get_or_create(language=Spanish, level='A2', hours='60')
        LevelsAndHour.objects.get_or_create(language=Spanish, level='B1', hours='90')
        LevelsAndHour.objects.get_or_create(language=Spanish, level='B2', hours='100')
        LevelsAndHour.objects.get_or_create(language=Spanish, level='C1', hours='120')
        LevelsAndHour.objects.get_or_create(language=Spanish, level='C2', hours='150')

        English, _=Language.objects.get_or_create(name='English')
        LevelsAndHour.objects.get_or_create(language=English, level='A1', hours='30')
        LevelsAndHour.objects.get_or_create(language=English, level='A2', hours='40')
        LevelsAndHour.objects.get_or_create(language=English, level='A3', hours='40')
        LevelsAndHour.objects.get_or_create(language=English, level='B1', hours='30')
        LevelsAndHour.objects.get_or_create(language=English, level='B2', hours='40')
        LevelsAndHour.objects.get_or_create(language=English, level='B3', hours='40')

        Japanese, _=Language.objects.get_or_create(name='Japanese')
        LevelsAndHour.objects.get_or_create(language=Japanese, level='N5', hours='90')
        LevelsAndHour.objects.get_or_create(language=Japanese, level='N4', hours='100')
        LevelsAndHour.objects.get_or_create(language=Japanese, level='N3', hours='110')
        LevelsAndHour.objects.get_or_create(language=Japanese, level='N2', hours='120')
        LevelsAndHour.objects.get_or_create(language=Japanese, level='N1', hours='150')

        Mandarin, _=Language.objects.get_or_create(name='Mandarin')
        LevelsAndHour.objects.get_or_create(language=Mandarin, level='HSK1', hours='40')
        LevelsAndHour.objects.get_or_create(language=Mandarin, level='HSK2', hours='40')
        LevelsAndHour.objects.get_or_create(language=Mandarin, level='HSK3', hours='40')
        LevelsAndHour.objects.get_or_create(language=Mandarin, level='HSK4', hours='40')
        LevelsAndHour.objects.get_or_create(language=Mandarin, level='HSK5', hours='40')

class NameOfCounselor(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='counselors_created_by')
    created_date = models.DateTimeField()
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='counselors_updated_by')
    updated_date = models.DateTimeField(null=True, blank=True,)

    def __str__(self):
        return self.name

class StudentTable(models.Model):

    FULL = 'Full'
    PART = 'Part'
    PAYMENT_TYPE_CHOICES = [
        (FULL, 'Full'),
        (PART, 'Part'),
    ]
    
    NEW_STUDENT = 'New Student'
    VERIFYD = 'Verified'
    BATCH_ALLOCATED = 'Batch Allocated'
    WAITING_FOR_ASSESSMENT = 'Waiting for Assessment'
    COURSE_COMPLETED = 'Course Completed'
    STATUS_CHOICES = [
        (NEW_STUDENT, 'New Student'),
        (VERIFYD, 'Verified'),
        (BATCH_ALLOCATED, 'Batch Allocated'),
        (WAITING_FOR_ASSESSMENT, 'Waiting for Assessment'),
        (COURSE_COMPLETED, 'Course Completed'),
    ]

    ONE_TO_ONE = 'One to One'
    GROUP = 'Group'
    BATCH_TYPE_CHOICES = [
        (ONE_TO_ONE, 'One to One'),
        (GROUP, 'Group'),
    ]

    STUDENT = 'Student'
    EMPLOYEE = 'Employee'
    SELF_EMPLOYEE = 'Self Employee'
    OTHERS = 'Others'
    PROFESSION_CHOICES = [
        (STUDENT, 'Student'),
        (EMPLOYEE, 'Employee'),
        (SELF_EMPLOYEE, 'Self Employee'),
        (OTHERS, 'Others'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Student_ID = models.CharField(unique=True, default=generate_customer_id, null=False, blank=False, max_length=20)
    Student_Name = models.CharField(max_length=100)
    Student_Phone_No = models.CharField(max_length=100)
    Student_Mail_Id = models.CharField(max_length=100)
    Student_Date_of_Birth = models.DateField(null=True, blank=True)
    Identity_Card_Aadhar_Copy = models.FileField(upload_to=Students_data, null=True, blank=True)
    Student_Photo = models.FileField(upload_to=Students_data, null=True, blank=True)
    Language_Name = models.ForeignKey(Language, on_delete=models.SET_NULL, blank=True, null=True)
    Level_and_Hour = models.ForeignKey(LevelsAndHour, on_delete=models.SET_NULL, blank=True, null=True)
    batch_preferences = models.ForeignKey(batch_preferences, on_delete=models.SET_NULL, blank=True, null=True)
    Batch_type = models.CharField(choices=BATCH_TYPE_CHOICES, max_length=20)
    
    Profession = models.CharField(choices=PROFESSION_CHOICES, max_length=20)
    Student_Counselor = models.ForeignKey(NameOfCounselor, on_delete=models.SET_NULL, blank=True, null=True)
    Payment_Type = models.CharField(choices=PAYMENT_TYPE_CHOICES, max_length=20)
    Transaction_ID = models.IntegerField()
    Account_Holder_Name = models.CharField(max_length=100)
    Amount_Paide = models.FloatField(default=0)
    Balance_Amount = models.FloatField(default=0)
    status = models.CharField(choices=STATUS_CHOICES, max_length=25)
    payment_complited = models.BooleanField(default=False)
    Created_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='students_created_by')
    Created_date = models.DateTimeField()
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='students_updated_by')
    Updated_date = models.DateTimeField(null=True, blank=True,)

    def __str__(self):
        return f'{self.Student_ID} -- {self.Student_Name}'

def Trainer_data(instance, filename):
    Year = dt.now().year
    return f'Trainer/{Year}/{instance.Trainer_ID}/{filename}'

def generate_trainer_id():
    Year = str(dt.now().year)
    last_trainer = TrainerTable.objects.order_by('-id').first()
    year = Year[2:]
    if last_trainer and last_trainer.Created_date.year == dt.now().year:
        last_id = int(last_trainer.Trainer_ID[7:])
        new_id = last_id + 1
    else:
        new_id = 1
    return f'INL{year}TR{new_id:04d}'

class TrainerTable(models.Model):
    Trainer_ID = models.CharField(unique=True, default=generate_trainer_id, null=False, blank=False, max_length=20)
    trainer_name = models.CharField(max_length=100)
    trainer_dob = models.DateField()
    trainer_education = models.CharField(max_length=100, null=True)
    trainer_mail = models.EmailField()
    trainer_phone = models.CharField(max_length=15) 
    trainer_languages = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, blank=True)
    trainer_address = models.TextField(max_length=500)
    trainer_photo = models.FileField(upload_to=Trainer_data)
    trainer_bank_details = models.CharField(max_length=100)
    trainer_aadhar = models.FileField(upload_to=Trainer_data)

    qualification = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    year_of_passing = models.CharField(max_length=4) 

    bank_account_number = models.IntegerField()
    bank_name = models.CharField(max_length=100)
    bank_branch = models.CharField(max_length=100)
    bank_ifsc = models.CharField(max_length=11)
    passbook = models.FileField(upload_to=Employee_data, null=True, blank=True)

    Created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='trainers_created_by')
    Created_date = models.DateTimeField()
    Updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='trainers_updated_by')
    Updated_date = models.DateTimeField(null=True, blank=True,)

    def __str__(self):
        return self.trainer_name

class BatchTiming(models.Model):
    batch_preferences = models.ForeignKey(batch_preferences, on_delete=models.CASCADE)
    timing = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.batch_preferences} -- {self.timing}"

@receiver(post_migrate)
def create_batch_timing(sender, **kwargs):
    if sender.name == 'Inlingua_app':
        weekdays, _ = batch_preferences.objects.get_or_create(batch_preferences='Weekdays')
        weekend, _ = batch_preferences.objects.get_or_create(batch_preferences='Weekend')

        BatchTiming.objects.get_or_create(
            batch_preferences=weekdays,
            timing='06:00 pm to 07:30 pm'
        )
        BatchTiming.objects.get_or_create(
            batch_preferences=weekdays,
            timing='07:00 pm to 08:30 pm'
        )
        BatchTiming.objects.get_or_create(
            batch_preferences=weekdays,
            timing='07:30 pm to 09:00 pm'
        )
        BatchTiming.objects.get_or_create(
            batch_preferences=weekend,
            timing='10:00 am to 01:00 pm'
        )
        BatchTiming.objects.get_or_create(
            batch_preferences=weekend,
            timing='02:00 pm to 05:00 pm'
        )

class Batch(models.Model):
    batch_name = models.CharField(unique=True, null=False, blank=False, max_length=20)
    levels = models.ForeignKey(LevelsAndHour, on_delete=models.SET_NULL,null=True, blank=True)
    batch_preferences = models.ForeignKey(batch_preferences, on_delete=models.SET_NULL,null=True, blank=True)
    students = models.ManyToManyField(StudentTable)
    time_slot = models.ForeignKey(BatchTiming, on_delete=models.SET_NULL,  null=True, blank=True)
    trainer = models.ForeignKey(TrainerTable, on_delete=models.SET_NULL, null=True, blank=True)
    course_start_date = models.DateField(null=True, blank=True)
    course_End_date = models.DateField(null=True, blank=True)

    Created_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='batch_created_by',null=True, blank=True)
    Created_date = models.DateTimeField()
    Updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='batch_updated_by')
    Updated_date = models.DateTimeField(null=True, blank=True,)

    def __str__(Self):
        return Self.batch_name
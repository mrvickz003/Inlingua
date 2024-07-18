from datetime import datetime as dt
from django.db import models
from django.contrib.auth.models import User

def Employee_data(instance, filename):
    Year = dt.now().year
    return f'Employee/{Year}/{instance.employee_ID}/{filename}'

def generate_employee_id():
    Year = str(dt.now().year)
    last_employee = employees.objects.order_by('-id').first()
    year = Year[2:]
    if last_employee and last_employee.Created_date.year == dt.now().year:
        last_id = int(last_employee.employee_ID[7:])
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

def Trainer_data(instance, filename):
    Year = dt.now().year
    return f'Students/{Year}/{instance.Student_ID}/{filename}'

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

class CurrentRole(models.Model):
    current_role = models.CharField(max_length=31)

class employees(models.Model):
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
    bank_account_number = models.IntegerField()
    bank_name = models.CharField(max_length=100)
    bank_branch = models.CharField(max_length=100)
    bank_ifsc = models.CharField(max_length=11)
    passbook = models.FileField(upload_to=Employee_data, null=True, blank=True)

    # Roles
    is_admin = models.BooleanField(default=False)
    is_business_manager = models.BooleanField(default=False)
    is_trainer_head = models.BooleanField(default=False)
    is_trainer = models.BooleanField(default=False)
    is_accoountant = models.BooleanField(default=False)
    is_business_development_executive = models.BooleanField(default=False)
    current_role = models.ForeignKey(CurrentRole, on_delete=models.CASCADE)

    Created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='employees_created_by')
    Created_date = models.DateTimeField()
    Updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='employees_updated_by')
    Updated_date = models.DateTimeField()

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='languages_created_by')
    created_date = models.DateTimeField()
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='languages_updated_by')
    updated_date = models.DateTimeField()

    def __str__(self):
        return self.name

class LevelsAndHour(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    level = models.CharField(max_length=5)
    help_text = models.CharField(max_length=100)
    hours = models.IntegerField()
    created_by = models.ForeignKey(employees, on_delete=models.CASCADE, related_name='levels_and_hours_created_by')
    created_date = models.DateTimeField()
    updated_by = models.ForeignKey(employees, on_delete=models.CASCADE, null=True, blank=True, related_name='levels_and_hours_updated_by')
    updated_date = models.DateTimeField()

    def __str__(self):
        return f"{self.language} -- {self.level} -- {self.hours} -- {self.help_text}"

class NameOfCounselor(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_by = models.ForeignKey(employees, on_delete=models.CASCADE, related_name='counselors_created_by')
    created_date = models.DateTimeField()
    updated_by = models.ForeignKey(employees, on_delete=models.CASCADE, null=True, blank=True, related_name='counselors_updated_by')
    updated_date = models.DateTimeField()

    def __str__(self):
        return self.name

class StudentTable(models.Model):
    WEEK_DAYS = 'Week Days'
    WEEKEND = 'Week End'
    COURSE_TYPE_CHOICES = [
        (WEEK_DAYS, 'Week Days'),
        (WEEKEND, 'Week End'),
    ]

    FULL = 'Full'
    PART = 'Part'
    PAYMENT_TYPE_CHOICES = [
        (FULL, 'Full'),
        (PART, 'Part'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Student_ID = models.CharField(unique=True, default=generate_customer_id, null=False, blank=False, max_length=20)
    Student_Name = models.CharField(max_length=100)
    Student_Phone_No = models.CharField(max_length=100)
    Student_Mail_Id = models.CharField(max_length=100)
    Student_Date_of_Birth = models.DateField(null=True, blank=True)
    Identity_Card_Aadhar_Copy = models.FileField(upload_to=Students_data, null=True, blank=True)
    Student_Photo = models.FileField(upload_to=Students_data, null=True, blank=True)
    Language_Name = models.ForeignKey(Language, on_delete=models.CASCADE)
    Level_and_Hour = models.ForeignKey(LevelsAndHour, on_delete=models.CASCADE)
    Course_Type = models.CharField(choices=COURSE_TYPE_CHOICES, max_length=20)
    Student_Counselor = models.ForeignKey(NameOfCounselor, on_delete=models.CASCADE)
    Payment_Type = models.CharField(choices=PAYMENT_TYPE_CHOICES, max_length=20)
    Transaction_ID = models.IntegerField()
    Account_Holder_Name = models.CharField(max_length=100)
    Amount_Paide = models.FloatField(default=0)
    Balance_Amount = models.FloatField(default=0)
    Created_by = models.ForeignKey(employees, on_delete=models.CASCADE, related_name='students_created_by')
    Created_date = models.DateTimeField()
    updated_by = models.ForeignKey(employees, on_delete=models.CASCADE, null=True, blank=True, related_name='students_updated_by')
    Updated_date = models.DateTimeField()

    def __str__(self):
        return f'{self.Student_ID} -- {self.Student_Name}'

class TrainerTable(models.Model):
    Trainer_ID = models.CharField(unique=True, default=generate_trainer_id, null=False, blank=False, max_length=20)
    trainer_name = models.CharField(max_length=100)
    trainer_dob = models.DateField()
    trainer_education = models.CharField(max_length=100)
    trainer_mail = models.EmailField()
    trainer_phone = models.CharField(max_length=15)  # Assuming phone number can include international format
    trainer_languages = models.CharField(max_length=100)
    trainer_address = models.TextField()
    trainer_photo = models.ImageField(upload_to=Trainer_data)
    trainer_bank_details = models.CharField(max_length=100)
    trainer_aadhar = models.CharField(max_length=12)  # Assuming Aadhar number has 12 digits
    trainer_role = models.CharField(max_length=100)  # Adjust max_length as per your role field requirements

    Created_by = models.ForeignKey(employees, on_delete=models.CASCADE, related_name='trainers_created_by')
    Created_date = models.DateTimeField()
    Updated_by = models.ForeignKey(employees, on_delete=models.CASCADE, null=True, blank=True, related_name='trainers_updated_by')
    Updated_date = models.DateTimeField()

    def __str__(self):
        return self.trainer_name

class TrainerQualifications(models.Model):
    trainer = models.ForeignKey(TrainerTable, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    year_of_passing = models.CharField(max_length=4)  # Assuming year is a 4-digit number

    def __str__(self):
        return f"{self.trainer} -- {self.qualification} -- {self.institution} -- {self.year_of_passing}"


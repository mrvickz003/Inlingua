import datetime as dt
from django.db import models
from django.contrib.auth.models import User

def Students_data(instance, filename):
    Year = dt.datetime.now().year
    return f'Students/{Year}/{instance.Student_ID}/{filename}'

def generate_customer_id():
    Year = str(dt.datetime.now().year)
    last_student = StudentTable.objects.order_by('-id').first()
    year = Year[2:]  # This ensures `year` is always assigned
    if last_student and last_student.Created_date.year == dt.datetime.now().year:
        last_id = int(last_student.Student_ID[7:])
        new_id = last_id + 1
    else:
        new_id = 1
    return f'ING{year}S{new_id:04d}'

class Language(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class LevelsAndHour(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    level = models.CharField(max_length=5)
    help_text = models.CharField(max_length=100)
    hours = models.IntegerField()
    created_by = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.language} -- {self.level} -- {self.hours} -- {self.help_text}"

class NameOfCounselor(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    created_by = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_by = models.CharField(max_length=100, null=True, blank=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    languages = models.ManyToManyField(Language)
    levels = models.ManyToManyField(LevelsAndHour)
    is_trainer_head = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class TrainerQualifications(models.Model):
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.trainer.user.username} - {self.qualification}"

class TrainingBatch(models.Model):
    name = models.CharField(max_length=255)
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

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
    Created_by = models.CharField(max_length=100)
    Created_date = models.DateTimeField(auto_now_add=True)
    Updated_by = models.CharField(max_length=100, null=True, blank=True)
    Updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.Student_ID} -- {self.Student_Name}'

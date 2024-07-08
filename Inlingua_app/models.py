from django.db import models

class language(models.Model):
    Language = models.CharField(max_length=100)
    Created_by = models.CharField(max_length=100)
    Created_date = models.DateTimeField()
    Updated_by = models.CharField(max_length=100, null=True, blank=True)
    Updated_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.Language
    
class levelsandhour(models.Model):
    Language = models.ForeignKey(language, on_delete=models.CASCADE)
    Level = models.CharField(max_length=5)
    Help_Text = models.CharField(max_length=100)
    Hours = models.IntegerField()
    Created_by = models.CharField(max_length=100)
    Created_date = models.DateTimeField()
    Updated_by = models.CharField(max_length=100, null=True, blank=True)
    Updated_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.Language} -- {self.Level} -- {self.Hours} -- {self.Help_Text}"
    
class nameOfCounselor(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=100)
    Phone = models.CharField(max_length=100)
    Created_by = models.CharField(max_length=100)
    Created_date = models.DateTimeField()
    Updated_by = models.CharField(max_length=100, null=True, blank=True)
    Updated_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.Name
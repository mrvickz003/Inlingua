# Generated by Django 5.0.4 on 2024-07-17 11:44

import Inlingua_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inlingua_app', '0014_alter_currentrole_current_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='aadhar_card',
            field=models.FileField(blank=True, null=True, upload_to=Inlingua_app.models.Employee_data),
        ),
    ]
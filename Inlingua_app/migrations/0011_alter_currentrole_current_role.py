# Generated by Django 5.0.4 on 2024-07-17 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inlingua_app', '0010_currentrole_rename_designation_employees_bank_branch_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentrole',
            name='current_role',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Business Manager', 'Business Manager'), ('Trainer Head', 'Trainer Head'), ('Accountant', 'Accoountant'), ('Business Development Executive', 'Business Development Executive')], max_length=30),
        ),
    ]
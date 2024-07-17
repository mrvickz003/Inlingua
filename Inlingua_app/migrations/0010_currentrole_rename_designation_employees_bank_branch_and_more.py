# Generated by Django 5.0.4 on 2024-07-17 09:39

import Inlingua_app.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inlingua_app', '0009_trainer_table_employee_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentRole',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_role', models.CharField(choices=[('Admin', 'Admin'), ('Business Manager', 'Business Manager'), ('Trainer Head', 'Trainer Head'), ('Trainer', 'Trainer'), ('Accountant', 'Accoountant'), ('Business Development Executive', 'Business Development Executive')], max_length=30)),
            ],
        ),
        migrations.RenameField(
            model_name='employees',
            old_name='designation',
            new_name='bank_branch',
        ),
        migrations.RemoveField(
            model_name='employees',
            name='date_of_birth',
        ),
        migrations.AddField(
            model_name='employees',
            name='bank_account_number',
            field=models.IntegerField(default=None, max_length=17),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employees',
            name='bank_ifsc',
            field=models.CharField(default=None, max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employees',
            name='bank_name',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employees',
            name='email',
            field=models.EmailField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employees',
            name='passbook',
            field=models.FileField(blank=True, null=True, upload_to=Inlingua_app.models.Employee_data),
        ),
        migrations.AddField(
            model_name='employees',
            name='current_role',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Inlingua_app.currentrole'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employees',
            name='Date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]

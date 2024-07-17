# Generated by Django 5.0.4 on 2024-07-17 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Inlingua_app', '0018_remove_employees_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='Created_by',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employees',
            name='Created_date',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employees',
            name='Updated_by',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='employees',
            name='Updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
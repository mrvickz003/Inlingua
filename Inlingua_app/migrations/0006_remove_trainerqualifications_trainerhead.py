from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Inlingua_app', '0005_trainerqualifications_trainerhead'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainerqualifications',
            name='trainerHead',
        ),
    ]
# Generated by Django 4.1.7 on 2023-03-06 06:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_onetimepassword_otp_num'),
    ]

    operations = [
       
        migrations.AddField(
            model_name='onetimepassword',
            name='date_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

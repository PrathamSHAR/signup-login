# Generated by Django 4.1.7 on 2023-03-06 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Onetimepassword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp_num', models.IntegerField(max_length=10)),
                ('username', models.CharField(max_length=50)),
                ('time_stamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

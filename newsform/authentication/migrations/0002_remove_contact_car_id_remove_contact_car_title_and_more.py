# Generated by Django 4.1.6 on 2023-03-04 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='car_id',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='car_title',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='city',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='customer_need',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='state',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='user_id',
        ),
    ]

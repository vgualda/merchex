# Generated by Django 4.2 on 2023-10-09 22:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_employee_telephone'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Telephone',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='registration',
        ),
    ]
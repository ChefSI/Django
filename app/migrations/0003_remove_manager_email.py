# Generated by Django 4.2 on 2024-02-26 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_establishment_module_teacher_module'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manager',
            name='email',
        ),
    ]

# Generated by Django 4.2 on 2024-02-26 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_teacher_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='email',
        ),
    ]

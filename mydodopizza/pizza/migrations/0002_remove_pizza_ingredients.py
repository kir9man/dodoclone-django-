# Generated by Django 4.1.1 on 2022-09-28 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizza',
            name='ingredients',
        ),
    ]
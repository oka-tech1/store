# Generated by Django 4.2.11 on 2024-07-24 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_alter_profile_msg'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactus',
            name='Email',
        ),
    ]

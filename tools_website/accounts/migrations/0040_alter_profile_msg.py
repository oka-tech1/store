# Generated by Django 4.2.11 on 2024-07-27 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0039_alter_profile_msg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='msg',
            field=models.TextField(default='Hello!! welcome, Place order and get your tool delivered to email', max_length=500),
        ),
    ]

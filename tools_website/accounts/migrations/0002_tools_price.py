# Generated by Django 5.0.7 on 2024-07-13 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tools',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]

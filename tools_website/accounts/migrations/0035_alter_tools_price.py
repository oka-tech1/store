# Generated by Django 4.2.11 on 2024-07-26 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0034_alter_tools_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tools',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]

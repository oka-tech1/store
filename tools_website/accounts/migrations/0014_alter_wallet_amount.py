# Generated by Django 5.0.7 on 2024-07-18 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_alter_wallet_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='amount',
            field=models.IntegerField(null=True),
        ),
    ]

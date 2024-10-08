# Generated by Django 5.0.7 on 2024-07-18 08:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_alter_users_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='wallet',
            new_name='userwallet',
        ),
        migrations.CreateModel(
            name='nameofuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(null=True)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.userwallet')),
            ],
        ),
        migrations.DeleteModel(
            name='users',
        ),
    ]

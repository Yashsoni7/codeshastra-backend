# Generated by Django 3.0.2 on 2020-03-07 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200307_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='women',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]

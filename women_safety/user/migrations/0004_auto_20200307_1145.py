# Generated by Django 3.0.2 on 2020-03-07 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200307_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='women',
            name='otp_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='women',
            name='emergency_contact1',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='women',
            name='emergency_contact2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='women',
            name='emergency_contact3',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='women',
            name='emergency_contact4',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='women',
            name='emergency_contact5',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='women',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]

# Generated by Django 2.2.6 on 2019-10-23 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gmidna', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flexstar',
            name='dateImported',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='flexstar',
            name='patientID',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='hospitaldata',
            name='dateImported',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='hospitaldata',
            name='patientID',
            field=models.CharField(max_length=20),
        ),
    ]

# Generated by Django 4.1.2 on 2023-02-10 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HospitalApp', '0005_auto_20221007_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_patient_information',
            name='health_card',
            field=models.CharField(default=123, max_length=10),
            preserve_default=False,
        ),
    ]
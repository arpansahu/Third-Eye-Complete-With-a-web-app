# Generated by Django 3.0.1 on 2020-01-18 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divyadrishti', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SumptomAndPatientName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientName', models.CharField(max_length=50)),
                ('symptomOne', models.CharField(max_length=50)),
                ('symptomTwo', models.CharField(max_length=50)),
                ('symptomThree', models.CharField(max_length=50)),
                ('symptomFour', models.CharField(max_length=50)),
                ('symptomFive', models.CharField(max_length=50)),
            ],
        ),
    ]

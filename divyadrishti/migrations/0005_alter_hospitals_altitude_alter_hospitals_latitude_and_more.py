# Generated by Django 4.0.3 on 2022-04-06 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divyadrishti', '0004_alter_hospitals_landline_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitals',
            name='altitude',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hospitals',
            name='latitude',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='hospitals',
            name='longitude',
            field=models.CharField(max_length=100),
        ),
    ]
# Generated by Django 4.0.3 on 2022-04-06 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('divyadrishti', '0003_hospitals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitals',
            name='landline_no',
            field=models.CharField(max_length=20),
        ),
    ]
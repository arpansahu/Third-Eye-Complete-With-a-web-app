# Generated by Django 4.0.3 on 2022-04-09 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('divyadrishti', '0010_rename_sumptomandpatientname_symptomsandpatientname_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SympTomsList',
            new_name='Symptoms',
        ),
    ]

# Generated by Django 3.1 on 2020-08-16 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Find_Hostel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostels',
            name='image',
            field=models.ImageField(default='', upload_to='Find_Hostel/images'),
        ),
    ]
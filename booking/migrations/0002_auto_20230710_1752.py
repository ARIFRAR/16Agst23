# Generated by Django 3.0.7 on 2023-07-10 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contact',
            new_name='Bookings',
        ),
    ]
# Generated by Django 3.0.7 on 2023-06-23 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0004_auto_20230623_0922'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wedding',
            old_name='waktu_pemasangan',
            new_name='durasi_acara',
        ),
    ]

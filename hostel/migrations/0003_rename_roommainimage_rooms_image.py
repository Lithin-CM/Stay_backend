# Generated by Django 4.0 on 2022-07-09 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hostel', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rooms',
            old_name='roomMainImage',
            new_name='image',
        ),
    ]

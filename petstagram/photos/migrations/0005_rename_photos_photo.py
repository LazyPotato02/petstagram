# Generated by Django 4.1.1 on 2022-10-15 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0004_alter_pet_slug'),
        ('photos', '0004_alter_photos_photo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Photos',
            new_name='Photo',
        ),
    ]

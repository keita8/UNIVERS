# Generated by Django 3.2.8 on 2021-11-01 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_auto_20211101_0825'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='user_photo',
            new_name='profile_picture',
        ),
    ]
# Generated by Django 3.2.8 on 2021-10-31 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured',
            field=models.BooleanField(default=False, verbose_name='Publié ?'),
        ),
    ]
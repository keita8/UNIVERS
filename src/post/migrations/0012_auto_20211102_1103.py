# Generated by Django 3.2.8 on 2021-11-02 10:03

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_auto_20211102_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=tinymce.models.HTMLField(verbose_name='Contenu'),
        ),
        migrations.AlterField(
            model_name='post',
            name='overview',
            field=tinymce.models.HTMLField(verbose_name='Apercu'),
        ),
    ]
# Generated by Django 3.2.8 on 2021-11-02 12:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0014_auto_20211102_1243'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='Date du commentaire')),
                ('content', models.TextField(verbose_name='Commentaire')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.post', verbose_name='Article commenté')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.author', verbose_name='Editeur ayant commenté')),
            ],
            options={
                'verbose_name': 'Commentaire',
                'verbose_name_plural': 'Commentaires',
            },
        ),
    ]

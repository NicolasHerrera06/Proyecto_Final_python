# Generated by Django 4.0.4 on 2022-07-03 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_contacto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posteo',
            name='imagenes',
        ),
    ]

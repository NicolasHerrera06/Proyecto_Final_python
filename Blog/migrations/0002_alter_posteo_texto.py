# Generated by Django 4.0.4 on 2022-07-02 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posteo',
            name='texto',
            field=models.TextField(),
        ),
    ]

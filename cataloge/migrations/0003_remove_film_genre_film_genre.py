# Generated by Django 4.2 on 2023-09-27 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cataloge', '0002_alter_film_runtime_minutes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='genre',
        ),
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.ManyToManyField(to='cataloge.genre'),
        ),
    ]

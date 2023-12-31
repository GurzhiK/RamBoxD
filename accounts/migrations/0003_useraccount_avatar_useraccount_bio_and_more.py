# Generated by Django 4.2 on 2023-09-27 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/'),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='username',
            field=models.CharField(default=5, max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]

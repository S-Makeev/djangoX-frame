# Generated by Django 4.2 on 2023-07-20 22:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie_crud', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='user',
            new_name='user_name',
        ),
    ]

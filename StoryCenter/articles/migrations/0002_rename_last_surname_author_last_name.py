# Generated by Django 4.1 on 2022-10-17 11:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='last_surname',
            new_name='last_name',
        ),
    ]
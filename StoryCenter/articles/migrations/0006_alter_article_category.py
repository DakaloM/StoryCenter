# Generated by Django 4.1.2 on 2022-10-25 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_alter_article_author_delete_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('Sport', 'Sport'), ('Entertainment', 'Entertainment'), ('Travel', 'Travel'), ('Lifestyle', 'Lifestyle'), ('Other', 'Other')], max_length=255),
        ),
    ]
# Generated by Django 5.0.7 on 2024-08-12 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_posts',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-08 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_home_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home_model',
            name='button_link',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='home_model',
            name='button_vid',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-10 09:08

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0021_alter_home_model_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home_model',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
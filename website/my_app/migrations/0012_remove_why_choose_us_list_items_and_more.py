# Generated by Django 4.2.4 on 2023-08-08 11:12

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0011_remove_home_model_button_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='why_choose_us',
            name='list_items',
        ),
        migrations.AddField(
            model_name='why_choose_us',
            name='sub_descripton',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='why_choose_us',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
    ]

# Generated by Django 4.2.4 on 2023-08-08 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0008_alter_home_model_button_link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='home_model',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='hero/'),
        ),
        migrations.AlterField(
            model_name='about_model',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

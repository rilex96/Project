# Generated by Django 4.0.5 on 2022-06-09 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_lokacija_event_location_alter_location_adresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='location_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
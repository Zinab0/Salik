# Generated by Django 4.2.11 on 2024-05-13 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic_light', '0006_alter_incident_date_alter_incident_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='incident',
            name='IntersectionID',
            field=models.IntegerField(default=2),
        ),
    ]
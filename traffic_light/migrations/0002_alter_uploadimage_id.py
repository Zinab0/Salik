# Generated by Django 4.2.11 on 2024-05-04 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic_light', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadimage',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
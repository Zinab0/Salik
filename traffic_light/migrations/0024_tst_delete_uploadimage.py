# Generated by Django 4.2.11 on 2024-05-17 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic_light', '0023_uploadimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='tst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
            ],
        ),
        # migrations.DeleteModel(
        #     name='UploadImage',
        # ),
    ]

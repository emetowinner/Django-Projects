# Generated by Django 3.0.3 on 2021-03-31 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_remove_job_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default='CSAM.png', upload_to='images/'),
        ),
    ]
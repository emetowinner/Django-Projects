# Generated by Django 3.0.3 on 2021-02-26 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]
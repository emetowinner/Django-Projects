# Generated by Django 3.0.3 on 2021-04-22 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_auto_20210422_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('favicon', models.CharField(max_length=400)),
                ('logo', models.CharField(max_length=400)),
                ('cv', models.CharField(max_length=400)),
            ],
        ),
    ]

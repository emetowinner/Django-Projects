# Generated by Django 3.0.3 on 2021-04-22 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_auto_20210422_1613'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldata',
            name='address',
            field=models.CharField(default='A108 Adam Street, New York, NY 535022', max_length=300),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='email',
            field=models.CharField(default='queeneomah@gmail.com', max_length=200),
        ),
        migrations.AddField(
            model_name='personaldata',
            name='phone',
            field=models.CharField(default='+234-704 0787 822', max_length=15),
        ),
    ]

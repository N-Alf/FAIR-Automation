# Generated by Django 2.1 on 2019-03-20 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_auto_20190321_0036'),
    ]

    operations = [
        migrations.AddField(
            model_name='reusability',
            name='ontUsed',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]

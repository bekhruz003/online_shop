# Generated by Django 4.0.6 on 2022-07-28 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_productmodel_real_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='sale',
            field=models.BooleanField(default=False, verbose_name='sale'),
        ),
    ]

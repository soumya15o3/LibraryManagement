# Generated by Django 3.1.5 on 2022-11-30 14:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0010_auto_20221129_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issuedbooks',
            name='return_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 15, 19, 47, 34, 952849)),
        ),
    ]

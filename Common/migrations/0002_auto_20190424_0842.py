# Generated by Django 2.1.4 on 2019-04-24 08:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loster',
            name='l_f_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 24, 8, 41, 43, 448989)),
        ),
        migrations.AlterField(
            model_name='loster',
            name='l_p_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 24, 8, 41, 43, 448989)),
        ),
        migrations.AlterField(
            model_name='loster',
            name='l_r_tel',
            field=models.IntegerField(),
        ),
    ]

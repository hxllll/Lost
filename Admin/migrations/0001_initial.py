# Generated by Django 2.1.4 on 2019-04-08 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_username', models.CharField(max_length=15, unique=True)),
                ('a_password', models.CharField(max_length=256)),
                ('is_delete', models.BooleanField(default=False)),
                ('is_super', models.BooleanField(default=False)),
            ],
        ),
    ]
# Generated by Django 3.2 on 2021-05-14 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='first_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

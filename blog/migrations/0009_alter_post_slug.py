# Generated by Django 3.2 on 2021-05-14 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_rename_author_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(help_text='add your blog slug means short url', max_length=100, unique=True),
        ),
    ]

# Generated by Django 2.2.1 on 2019-07-01 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_post_published_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
    ]

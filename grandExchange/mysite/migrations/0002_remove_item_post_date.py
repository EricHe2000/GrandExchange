# Generated by Django 2.2.4 on 2020-02-10 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='post_date',
        ),
    ]

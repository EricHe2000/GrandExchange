# Generated by Django 2.2.4 on 2020-03-17 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authenticator',
            fields=[
                ('user_id', models.IntegerField(default=0)),
                ('authenticator', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('is_Valid', models.BooleanField(default=True)),
                ('date_created', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sold', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('numberBought', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uniquename', models.CharField(max_length=50)),
                ('password', models.CharField(default='none', max_length=50)),
                ('first_name', models.CharField(default='none', max_length=50)),
                ('last_name', models.CharField(default='none', max_length=50)),
                ('age', models.DecimalField(decimal_places=0, default='none', max_digits=3)),
                ('email', models.CharField(default='none', max_length=50)),
            ],
        ),
    ]

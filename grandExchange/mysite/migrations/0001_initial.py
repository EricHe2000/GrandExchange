# Generated by Django 2.2.4 on 2020-02-09 19:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('age', models.DecimalField(decimal_places=0, max_digits=3)),
                ('gender', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sold', models.BooleanField(default=False)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=150)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
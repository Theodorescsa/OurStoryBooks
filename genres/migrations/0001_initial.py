# Generated by Django 4.2.6 on 2024-07-09 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenresModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genres', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]

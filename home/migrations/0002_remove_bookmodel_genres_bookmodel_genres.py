# Generated by Django 4.2.6 on 2024-07-09 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genres', '0001_initial'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookmodel',
            name='genres',
        ),
        migrations.AddField(
            model_name='bookmodel',
            name='genres',
            field=models.ManyToManyField(to='genres.genresmodel'),
        ),
    ]
# Generated by Django 4.2.6 on 2024-07-09 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_bookmodel_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='book_image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]

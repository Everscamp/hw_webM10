# Generated by Django 5.0.6 on 2024-06-02 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quoteapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='born_date',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='author',
            name='born_location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='author',
            name='fullname',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]

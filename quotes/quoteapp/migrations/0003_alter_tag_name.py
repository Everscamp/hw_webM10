# Generated by Django 5.0.6 on 2024-06-02 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quoteapp', '0002_alter_author_born_date_alter_author_born_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
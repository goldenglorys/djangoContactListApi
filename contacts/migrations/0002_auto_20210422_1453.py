# Generated by Django 3.0.7 on 2021-04-22 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='is_favorite',
            field=models.BooleanField(default=False),
        ),
    ]

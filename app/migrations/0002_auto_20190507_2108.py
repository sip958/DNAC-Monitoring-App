# Generated by Django 2.2.1 on 2019-05-07 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='network',
            name='ip',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
# Generated by Django 5.1.3 on 2024-11-20 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reg_tbl',
            name='mb',
            field=models.IntegerField(),
        ),
    ]
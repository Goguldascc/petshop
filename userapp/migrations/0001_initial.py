# Generated by Django 5.1.3 on 2024-11-19 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='reg_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fn', models.CharField(max_length=50)),
                ('mb', models.ImageField(upload_to='')),
                ('em', models.EmailField(max_length=254)),
                ('ps', models.CharField(max_length=16)),
                ('cps', models.CharField(max_length=16)),
            ],
        ),
    ]
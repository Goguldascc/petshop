# Generated by Django 5.1.3 on 2024-12-02 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_alter_reg_tbl_mb'),
    ]

    operations = [
        migrations.CreateModel(
            name='pro_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pnm', models.CharField(max_length=25)),
                ('pim', models.FileField(upload_to='pic')),
                ('prc', models.IntegerField()),
                ('des', models.TextField()),
            ],
        ),
    ]
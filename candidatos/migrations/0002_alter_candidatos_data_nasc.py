# Generated by Django 4.1.1 on 2022-09-16 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('candidatos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatos',
            name='data_nasc',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

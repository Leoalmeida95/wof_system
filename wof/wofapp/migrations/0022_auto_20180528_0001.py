# Generated by Django 2.0 on 2018-05-28 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wofapp', '0021_auto_20180526_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helloworld',
            name='codigo_exemplo',
            field=models.CharField(max_length=50000),
        ),
        migrations.AlterField(
            model_name='helloworld',
            name='descricao',
            field=models.CharField(max_length=50000),
        ),
    ]

# Generated by Django 2.0 on 2018-05-26 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wofapp', '0020_auto_20180526_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comentario',
            name='respostas',
            field=models.ManyToManyField(to='wofapp.Comentario'),
        ),
    ]

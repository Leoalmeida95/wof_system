# Generated by Django 2.0 on 2018-04-18 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wofapp', '0006_usuario_is_activeuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='data',
            field=models.DateField(auto_now=True),
        ),
    ]

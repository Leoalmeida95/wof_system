# Generated by Django 2.0 on 2018-04-18 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wofapp', '0007_usuario_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='data',
            new_name='data_Cadastro',
        ),
    ]

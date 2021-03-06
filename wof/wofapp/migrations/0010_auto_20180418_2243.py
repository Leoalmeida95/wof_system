# Generated by Django 2.0 on 2018-04-19 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wofapp', '0009_auto_20180418_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(help_text='O campo CPF é obriagatório.', max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(help_text='O campo Email é obrigatório.', max_length=100, unique=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='first_name',
            field=models.CharField(help_text='O campo Nome é obrigatório.', max_length=50, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='last_name',
            field=models.CharField(help_text='O campo Sobrenome é obrigatório.', max_length=50, verbose_name='Sobrenome'),
        ),
    ]

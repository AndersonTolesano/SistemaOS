# Generated by Django 2.2.6 on 2019-11-28 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20191128_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordemservico',
            name='dataAtendimento',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ordemservico',
            name='responsavel',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ordemservico',
            name='tipoDeAtendimento',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

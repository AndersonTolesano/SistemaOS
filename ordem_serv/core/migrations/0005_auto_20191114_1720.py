# Generated by Django 2.2.6 on 2019-11-14 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20191114_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novocliente',
            name='cnpj',
            field=models.TextField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
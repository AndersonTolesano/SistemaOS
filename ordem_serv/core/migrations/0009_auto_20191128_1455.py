# Generated by Django 2.2.6 on 2019-11-28 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20191127_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='anexo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='tipo_atendimento',
            field=models.CharField(choices=[('0', 'Selecione'), ('1', 'Presencial'), ('2', 'Remoto'), ('3', 'Projeto')], default='1', max_length=1),
        ),
    ]
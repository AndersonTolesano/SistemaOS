# Generated by Django 2.2.6 on 2019-11-26 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20191120_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitante',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='core.NovoCliente'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='tipo_atendimento',
            field=models.CharField(choices=[('1', ' '), ('2', 'Presencial'), ('3', 'Remoto'), ('4', 'Projeto')], default='1', max_length=1),
        ),
    ]

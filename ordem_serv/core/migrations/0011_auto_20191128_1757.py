# Generated by Django 2.2.6 on 2019-11-28 20:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20191128_1511'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordemservico',
            name='apagado',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ordemservico',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]

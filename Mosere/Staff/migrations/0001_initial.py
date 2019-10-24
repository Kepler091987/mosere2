# Generated by Django 2.2.6 on 2019-10-24 03:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre Completo')),
                ('phone', models.BigIntegerField(verbose_name='Telefono')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo')),
                ('entry_date', models.DateField(verbose_name='Fecha de ingreso')),
                ('market_stall', models.CharField(choices=[('ADM', 'Administrador'), ('INS', 'Instalador'), ('ING', 'Ingeniero')], max_length=3, verbose_name='Puesto')),
                ('Rol', models.CharField(choices=[('ADM', 'Administrador'), ('INS', 'Instalador'), ('ING', 'Ingeniero')], max_length=3, verbose_name='Rol')),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Personal',
                'verbose_name_plural': 'Personal',
                'ordering': ['created_on'],
            },
        ),
    ]

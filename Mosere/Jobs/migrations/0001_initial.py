# Generated by Django 2.2.6 on 2019-10-24 03:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Clients', '0001_initial'),
        ('Staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_folio', models.CharField(max_length=100, verbose_name='Numero de Folio')),
                ('description', models.TextField(max_length=500, verbose_name='Descripción')),
                ('time', models.TimeField(verbose_name='Tiempo aproximado')),
                ('date_start', models.DateTimeField(verbose_name='Fecha de inicio')),
                ('date_end', models.DateTimeField(verbose_name='Fecha de termino')),
                ('scheduled_date', models.DateTimeField(verbose_name='Fecha programada')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Clients.Clients', verbose_name='cliente')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Staff.Staff', verbose_name='Personal')),
            ],
            options={
                'verbose_name': 'Trabajo',
                'verbose_name_plural': 'Trabajos',
                'ordering': ['created_on'],
            },
        ),
    ]

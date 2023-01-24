# Generated by Django 4.0.6 on 2022-12-09 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PedidoMedidores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido', models.CharField(default=0, max_length=100, null=True)),
                ('municipio', models.CharField(default=0, max_length=100, null=True)),
                ('actividad', models.CharField(default=0, max_length=100, null=True)),
                ('pagina', models.CharField(default=0, max_length=100, null=True)),
                ('item_cont', models.CharField(default=0, max_length=100, null=True)),
                ('suminis', models.CharField(default=0, max_length=100, null=True)),
                ('cantidad', models.CharField(default=0, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Acta Medidores',
                'verbose_name_plural': 'Acta Medidoress',
            },
        ),
        migrations.CreateModel(
            name='NovedadMedidores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('novedad', models.CharField(default=0, max_length=200, null=True)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medidores.pedidomedidores')),
            ],
            options={
                'verbose_name': 'Novedades Medidores',
                'verbose_name_plural': 'Novedades Medidoress',
            },
        ),
    ]

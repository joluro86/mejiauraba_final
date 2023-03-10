# Generated by Django 4.0.6 on 2022-12-09 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Despacho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100, verbose_name='Código')),
                ('fecha', models.CharField(max_length=500, verbose_name='Fecha')),
                ('encargado', models.CharField(default='0', max_length=500, verbose_name='Encargado')),
                ('cantidad', models.CharField(default='0', max_length=100, verbose_name='Cantidad')),
            ],
            options={
                'verbose_name': 'Despacho oficial',
                'verbose_name_plural': 'Despachos oficiales',
            },
        ),
        migrations.CreateModel(
            name='Inicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('encargado', models.CharField(max_length=500, verbose_name='Oficial')),
                ('codigo', models.CharField(max_length=100, verbose_name='Código')),
                ('cantidad', models.CharField(max_length=100, verbose_name='Cantidad')),
            ],
            options={
                'verbose_name': 'Cantidadi Inicio Oficial',
                'verbose_name_plural': 'Cantidad Inicio Oficial',
            },
        ),
        migrations.CreateModel(
            name='Liquidacion_acta_epm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido', models.CharField(max_length=10, verbose_name='Pedido')),
                ('actividad', models.CharField(max_length=500, verbose_name='Actividad')),
                ('item_cont', models.CharField(max_length=100, verbose_name='item_cont')),
                ('cantidad', models.CharField(max_length=100, verbose_name='Cantidad')),
                ('encargado', models.CharField(default='0', max_length=100, verbose_name='Encargado')),
                ('conc_pedido_codigo', models.CharField(default='0', max_length=100, verbose_name='concatenacion')),
            ],
            options={
                'verbose_name': 'Liquidación Acta Epm',
                'verbose_name_plural': 'Liquidación Acta Epm',
            },
        ),
        migrations.CreateModel(
            name='Material_A_Buscar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='--', max_length=500, verbose_name='Oficial')),
            ],
            options={
                'verbose_name': 'Material a buscar',
                'verbose_name_plural': 'Material a buscar',
            },
        ),
        migrations.CreateModel(
            name='Material_utilizado_perseo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido', models.CharField(max_length=10, verbose_name='Pedido')),
                ('actividad', models.CharField(default='0', max_length=500, verbose_name='Actividad')),
                ('instalador', models.CharField(max_length=500, verbose_name='Instalador')),
                ('fecha', models.CharField(max_length=100, verbose_name='Fecha')),
                ('codigo', models.CharField(max_length=100, verbose_name='Código')),
                ('cantidad', models.CharField(default='0', max_length=100, verbose_name='Cantidad')),
                ('conc_pedido_codigo', models.CharField(default='0', max_length=100, verbose_name='concatenacion')),
            ],
            options={
                'verbose_name': 'Material Utilizado Perseo',
                'verbose_name_plural': 'Material Utilizado Perseo',
            },
        ),
        migrations.CreateModel(
            name='Oficial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500, verbose_name='Oficial')),
            ],
            options={
                'verbose_name': 'Oficial',
                'verbose_name_plural': 'Oficiales',
            },
        ),
        migrations.CreateModel(
            name='Reintegro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100, verbose_name='Código')),
                ('fecha', models.CharField(max_length=500, verbose_name='Fecha')),
                ('encargado', models.CharField(default='0', max_length=500, verbose_name='Encargado')),
                ('cantidad', models.CharField(default='0', max_length=100, verbose_name='Cantidad')),
            ],
            options={
                'verbose_name': 'Reintegro oficial',
                'verbose_name_plural': 'Reintegros oficiales',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('encargado', models.CharField(default='0', max_length=300, verbose_name='Oficial')),
                ('codigo', models.CharField(default='0', max_length=100, verbose_name='Código')),
                ('inicio', models.CharField(default='0', max_length=100, verbose_name='Inicio')),
                ('despachado', models.CharField(default='0', max_length=100, verbose_name='Despachado')),
                ('reintegrado', models.CharField(default='0', max_length=100, verbose_name='Reintegrado')),
                ('epm', models.CharField(default='0', max_length=100, verbose_name='Epm')),
                ('diferencia', models.CharField(default='0', max_length=100, verbose_name='Diferencia')),
            ],
            options={
                'verbose_name': 'Stock',
                'verbose_name_plural': 'Stock',
            },
        ),
    ]

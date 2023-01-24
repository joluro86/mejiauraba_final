# Generated by Django 4.0.6 on 2022-12-19 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Acta_analisis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pedido', models.CharField(default=0, max_length=100)),
                ('municipio', models.CharField(default=0, max_length=100)),
                ('actividad', models.CharField(default=0, max_length=100)),
                ('pagina', models.CharField(default=0, max_length=100)),
                ('urbrur', models.CharField(default=0, max_length=100)),
                ('tipre', models.CharField(default=0, max_length=100)),
                ('tipo', models.CharField(default=0, max_length=100)),
                ('suminis', models.CharField(default=0, max_length=100)),
                ('item_cont', models.CharField(default=0, max_length=100)),
                ('cantidad', models.CharField(default=0, max_length=100)),
            ],
            options={
                'verbose_name': 'Acta_analisis',
                'verbose_name_plural': 'Acta_analisis',
                'ordering': ['pedido'],
            },
        ),
    ]

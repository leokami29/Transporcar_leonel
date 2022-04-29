# Generated by Django 4.0.4 on 2022-04-26 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=10)),
                ('modelo', models.IntegerField(default=2021)),
                ('marca', models.CharField(max_length=30)),
                ('Capacidad', models.IntegerField(default=1)),
                ('conductor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personas.conductor')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personas.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Infraccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('description', models.CharField(max_length=30)),
                ('valor', models.IntegerField(default=1)),
                ('conductor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='personas.conductor')),
                ('vehiculo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehiculos.vehiculo')),
            ],
        ),
    ]
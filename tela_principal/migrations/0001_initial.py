# Generated by Django 3.2.9 on 2021-11-11 00:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('data', models.DateField()),
                ('descricao', models.TextField()),
                ('atas', models.FileField(upload_to='atas')),
            ],
            options={
                'verbose_name': 'Ata',
                'verbose_name_plural': 'Atas',
            },
        ),
        migrations.CreateModel(
            name='Avisos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('data', models.DateField()),
                ('descricao', models.TextField()),
                ('avisos', models.FileField(upload_to='avisos')),
            ],
            options={
                'verbose_name': 'Aviso',
                'verbose_name_plural': 'Avisos',
            },
        ),
        migrations.CreateModel(
            name='Outros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('data', models.DateField()),
                ('descricao', models.TextField()),
                ('outros', models.FileField(upload_to='outros')),
            ],
            options={
                'verbose_name': 'Outro',
                'verbose_name_plural': 'Outros',
            },
        ),
        migrations.CreateModel(
            name='Comentarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comentario', models.TextField()),
                ('data', models.DateTimeField(default=datetime.datetime.now)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='usuarios.usuario')),
            ],
        ),
    ]
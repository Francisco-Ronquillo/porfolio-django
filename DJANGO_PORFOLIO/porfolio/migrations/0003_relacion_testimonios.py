# Generated by Django 5.1.1 on 2024-10-07 19:02

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('porfolio', '0002_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_test', models.CharField(max_length=30)),
                ('testimonio', models.CharField(max_length=100)),
                ('fecha_testimonio', models.DateField(default=datetime.date.today)),
                ('relacion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='porfolio.relacion')),
            ],
        ),
    ]

# Generated by Django 5.1.1 on 2024-09-29 00:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='descripcion',
            new_name='description',
        ),
    ]
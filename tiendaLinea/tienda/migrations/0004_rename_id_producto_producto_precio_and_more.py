# Generated by Django 4.0.4 on 2022-06-22 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_rename_nombre_cliente_cliente_nombre_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='id_producto',
            new_name='precio',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='id_cliente',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='precio_producto',
        ),
    ]

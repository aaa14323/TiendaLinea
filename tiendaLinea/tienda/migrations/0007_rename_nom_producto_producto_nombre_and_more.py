# Generated by Django 4.0.4 on 2022-06-25 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0006_cliente_cantidad'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='nom_producto',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='producto',
        ),
        migrations.AddField(
            model_name='cliente',
            name='estado',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordenados', models.BooleanField(default=False)),
                ('fechaPedido', models.DateTimeField(auto_now=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tienda.cliente')),
                ('producto', models.ManyToManyField(to='tienda.producto')),
            ],
        ),
    ]

# Generated by Django 5.1 on 2024-10-27 05:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_rename_pedido_id_lineapedido_pedido_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lineapedido',
            options={'ordering': ['id'], 'verbose_name': 'Línea Pedido', 'verbose_name_plural': 'Líneas de Pedido'},
        ),
    ]

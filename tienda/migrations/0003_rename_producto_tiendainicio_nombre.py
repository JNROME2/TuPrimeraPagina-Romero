# Generated by Django 5.2 on 2025-04-26 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_tiendainicio_rename_precio_tiendaproductos_codigo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tiendainicio',
            old_name='producto',
            new_name='nombre',
        ),
    ]

# Generated by Django 4.1.5 on 2023-02-02 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0005_bicicletas_decuento_bicicletas_imagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bicicletas',
            old_name='decuento',
            new_name='descuento',
        ),
    ]

# Generated by Django 4.1.5 on 2023-02-02 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_alter_indumentaria_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='bicicletas',
            name='decuento',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='bicicletas',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='fotos_productos'),
        ),
    ]

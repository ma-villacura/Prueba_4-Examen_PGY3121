# Generated by Django 4.0.5 on 2022-06-14 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_delete_fundacion_producto_imagenprod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagenProd',
            field=models.ImageField(null=True, upload_to='static/img'),
        ),
    ]

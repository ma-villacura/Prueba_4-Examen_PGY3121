from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    
    initial = True
    
    dependencies = [

    ]

    operations= [
        migrations.CreateModel(
            name='CategoriaProd',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Categoria')),
                ('nombreCategoria', models.CharField(max_length=50, verbose_name='Nombre de la categoria')),
            ],   
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codProducto',models.CharField(max_lenght=6, primary_key=True, serialize=False, verbose_name='Codigo Producto')),
                ('nombreProducto', models.CharField(max_length=50, verbose_name="Nombre producto")),
                ('descripcion',models.CharField(max_length=50, verbose_name="Descripccion Producto")),
                ('stock',models.IntegerField( verbose_name="Cantidad Disponible")),
                ('precio',models.IntegerField( verbose_name="Precio Producto")),
                ('fotoProd', models.ImageField(upload_to='static/img/')),
                ('categoria',models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CategoriaProd')),
        
               
            ],
        ),
    ]
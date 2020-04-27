# Generated by Django 2.2.10 on 2020-04-27 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('descripcion', models.TextField()),
                ('precio', models.FloatField(default=10, null=True)),
                ('stock', models.IntegerField(default=10, null=True)),
                ('tipo', models.CharField(max_length=1, null=True)),
                ('imagen', models.ImageField(upload_to='static/imgPro')),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subTotal', models.FloatField()),
                ('cantidad', models.IntegerField(default=1, null=True)),
                ('idUser', models.IntegerField(default=1, null=True)),
                ('idPro', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comercio.Producto')),
            ],
        ),
    ]

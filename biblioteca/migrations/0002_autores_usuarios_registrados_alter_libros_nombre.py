# Generated by Django 4.2.4 on 2023-08-15 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('nacimiento', models.IntegerField()),
                ('obra_destacada', models.CharField(max_length=150)),
                ('biografia', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios_registrados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=40)),
                ('clave', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='libros',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 4.0.4 on 2022-05-02 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hermana',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('Edad', models.IntegerField()),
                ('color_favorito', models.CharField(max_length=30)),
                ('fecha_de_nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Madre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('Edad', models.IntegerField()),
                ('color_favorito', models.CharField(max_length=30)),
                ('fecha_de_nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Novia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('Edad', models.IntegerField()),
                ('color_favorito', models.CharField(max_length=30)),
                ('fecha_de_nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Padre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('Edad', models.IntegerField()),
                ('color_favorito', models.CharField(max_length=30)),
                ('fecha_de_nacimiento', models.DateField()),
            ],
        ),
    ]

# Generated by Django 3.0.7 on 2020-06-29 23:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=140)),
                ('sinopsis', models.TextField(blank=True, null=True)),
                ('duracion', models.PositiveIntegerField()),
                ('calif', models.PositiveIntegerField(default=5)),
                ('genero', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

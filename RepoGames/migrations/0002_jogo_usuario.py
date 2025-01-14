# Generated by Django 2.1.7 on 2019-04-21 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RepoGames', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('descricao', models.TextField()),
                ('fotos', models.TextField()),
                ('arquivo', models.FileField(upload_to='uploads/%Y/%m/%d/%H/%M/%S/')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('senha', models.CharField(max_length=16)),
            ],
        ),
    ]

# Generated by Django 2.1.7 on 2019-04-21 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RepoGames', '0002_jogo_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jogo',
            name='fotos',
        ),
        migrations.AddField(
            model_name='jogo',
            name='foto1',
            field=models.ImageField(blank=True, upload_to='uploads/%Y/%m/%d/%H/%M/%S/'),
        ),
        migrations.AddField(
            model_name='jogo',
            name='foto2',
            field=models.ImageField(blank=True, upload_to='uploads/%Y/%m/%d/%H/%M/%S/'),
        ),
        migrations.AddField(
            model_name='jogo',
            name='foto3',
            field=models.ImageField(blank=True, upload_to='uploads/%Y/%m/%d/%H/%M/%S/'),
        ),
    ]

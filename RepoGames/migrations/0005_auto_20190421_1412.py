# Generated by Django 2.1.7 on 2019-04-21 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RepoGames', '0004_auto_20190421_1335'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Document',
        ),
        migrations.AlterField(
            model_name='jogo',
            name='foto1',
            field=models.ImageField(blank=True, upload_to='uploads/imagens/%Y/%m/%d/%H/%M/%S/'),
        ),
        migrations.AlterField(
            model_name='jogo',
            name='foto2',
            field=models.ImageField(blank=True, upload_to='uploads/imagens/%Y/%m/%d/%H/%M/%S/'),
        ),
        migrations.AlterField(
            model_name='jogo',
            name='foto3',
            field=models.ImageField(blank=True, upload_to='uploads/imagens/%Y/%m/%d/%H/%M/%S/'),
        ),
    ]

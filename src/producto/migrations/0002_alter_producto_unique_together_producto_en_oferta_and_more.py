# Generated by Django 4.2.20 on 2025-04-08 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='producto',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='producto',
            name='en_oferta',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='producto',
            name='estrellas',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='productos/'),
        ),
        migrations.AddField(
            model_name='producto',
            name='mostrar_estrellas',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='producto',
            name='precio_original',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(blank=True, default=' sin descripcion '),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.RemoveField(
            model_name='producto',
            name='categoria',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='stock',
        ),
    ]

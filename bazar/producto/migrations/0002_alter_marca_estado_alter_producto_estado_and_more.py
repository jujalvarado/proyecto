# Generated by Django 4.1 on 2022-09-11 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marca',
            name='estado',
            field=models.SmallIntegerField(default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='producto',
            name='estado',
            field=models.SmallIntegerField(default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='proveedor',
            name='estado',
            field=models.SmallIntegerField(default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='proveedor_marca',
            name='estado',
            field=models.SmallIntegerField(default=1, max_length=1),
        ),
    ]
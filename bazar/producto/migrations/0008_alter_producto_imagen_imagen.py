# Generated by Django 4.1 on 2022-09-16 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0007_alter_producto_imagen_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto_imagen',
            name='imagen',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
    ]

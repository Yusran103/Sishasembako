# Generated by Django 3.0.3 on 2020-05-07 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sishasembapo', '0009_auto_20200410_1018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sembako',
            name='satuan',
            field=models.CharField(choices=[('Kg', 'Kg'), ('Perbiji', 'Perbiji'), ('Liter', 'Liter')], default='Kg', max_length=20),
        ),
    ]
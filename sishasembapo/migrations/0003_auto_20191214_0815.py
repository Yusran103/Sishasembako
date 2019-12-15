# Generated by Django 2.2.6 on 2019-12-14 01:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sishasembapo', '0002_auto_20191214_0801'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sembako',
            old_name='nama',
            new_name='jenis_sembako',
        ),
        migrations.AddField(
            model_name='sembako',
            name='nama_sembako',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sishasembapo.Sembako'),
        ),
    ]
# Generated by Django 3.0.3 on 2020-05-07 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sishasembapo', '0011_delete_satuan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Satuan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('satuan', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Satuan',
                'db_table': 'Tb_Satuan',
            },
        ),
    ]

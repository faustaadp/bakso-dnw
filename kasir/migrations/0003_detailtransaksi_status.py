# Generated by Django 3.2.16 on 2023-01-13 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kasir', '0002_detailtransaksi_transaksi'),
    ]

    operations = [
        migrations.AddField(
            model_name='detailtransaksi',
            name='status',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]

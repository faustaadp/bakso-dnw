# Generated by Django 3.2.16 on 2023-01-13 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kasir', '0004_alter_transaksi_waktu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='detailtransaksi',
            name='status',
        ),
        migrations.AddField(
            model_name='transaksi',
            name='status',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.1.2 on 2023-01-14 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kasir', '0007_transaksi_total_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detailtransaksi',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='kategori',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='transaksi',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
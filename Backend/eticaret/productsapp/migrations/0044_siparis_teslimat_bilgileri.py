# Generated by Django 4.2.3 on 2023-08-09 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0043_siparis_siparisurun_delete_odeme_siparis_urunler_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='siparis',
            name='teslimat_bilgileri',
            field=models.CharField(max_length=200, null=True, verbose_name='Teslimat Bilgileri'),
        ),
    ]
# Generated by Django 4.2.3 on 2023-08-09 20:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('productsapp', '0046_remove_siparis_teslimat_bilgileri_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='siparis',
            name='gönderim_bilgisi',
            field=models.BooleanField(default=False, verbose_name='Ürün Gönderim Bilgisi'),
        ),
        migrations.AlterField(
            model_name='siparis',
            name='teslimat_bilgileri_adres',
            field=models.TextField(max_length=200, null=True, verbose_name='Adress'),
        ),
        migrations.AlterField(
            model_name='siparis',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı Adı'),
        ),
    ]

# Generated by Django 4.2.3 on 2023-08-09 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0041_remove_odeme_sepet_odeme_sepet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='odeme',
            name='sepet',
        ),
        migrations.AddField(
            model_name='odeme',
            name='sepet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='productsapp.sepet'),
        ),
    ]

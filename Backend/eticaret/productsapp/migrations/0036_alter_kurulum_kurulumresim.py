# Generated by Django 4.2.3 on 2023-08-03 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0035_alter_kurulum_video_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kurulum',
            name='kurulumResim',
            field=models.ImageField(blank=True, null=True, upload_to='kurulum/', verbose_name='Kurulum Resmi 6'),
        ),
    ]

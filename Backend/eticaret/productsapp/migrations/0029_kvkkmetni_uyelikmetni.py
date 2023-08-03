# Generated by Django 4.2.3 on 2023-08-03 08:38

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0028_hakkimizda'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kvkkmetni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kvkkBaslik', models.CharField(max_length=100, null=True)),
                ('kvkkmetni', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='KVKK Metni')),
            ],
            options={
                'verbose_name_plural': 'KVKK Metni',
            },
        ),
        migrations.CreateModel(
            name='Uyelikmetni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uyelikBaslik', models.CharField(max_length=100, null=True)),
                ('uyelikmetni', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Üyelik Metni')),
            ],
            options={
                'verbose_name_plural': 'Üyelik Metni',
            },
        ),
    ]

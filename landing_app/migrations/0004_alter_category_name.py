# Generated by Django 4.0.5 on 2022-06-23 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_app', '0003_alter_product_date_added'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, verbose_name='категория'),
        ),
    ]

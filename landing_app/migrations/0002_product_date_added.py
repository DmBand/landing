# Generated by Django 4.0.5 on 2022-06-23 08:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('landing_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_added',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='дата добавления'),
            preserve_default=False,
        ),
    ]

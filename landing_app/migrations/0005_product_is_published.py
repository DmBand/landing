# Generated by Django 4.0.5 on 2022-06-23 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing_app', '0004_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=True, verbose_name='опубликовано'),
        ),
    ]

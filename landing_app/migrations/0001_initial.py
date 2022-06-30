# Generated by Django 4.0.5 on 2022-06-23 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='категория')),
            ],
            options={
                'verbose_name': 'категория',
                'verbose_name_plural': 'категории',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название изделия')),
                ('description', models.TextField(verbose_name='описание')),
                ('price', models.FloatField(verbose_name='цена')),
                ('image', models.ImageField(upload_to='', verbose_name='фото')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landing_app.category', verbose_name='категория')),
            ],
            options={
                'verbose_name': 'изделие',
                'verbose_name_plural': 'изделия',
            },
        ),
    ]

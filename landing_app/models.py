from django.db import models

from .compression import compress_product_image
from landing import settings


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    TIME_TO_COMPRESS = 60
    PHOTO_CUALITY = 30

    name = models.CharField(max_length=100, verbose_name='название изделия')
    description = models.TextField(verbose_name='описание')
    price = models.FloatField(verbose_name='цена', blank=True, null=True)
    price_per_kg = models.FloatField(verbose_name='цена за 1кг', blank=True, null=True)
    price_per_100g = models.FloatField(verbose_name='цена за 100гр', blank=True, null=True)
    image = models.ImageField(verbose_name='фото')
    is_published = models.BooleanField(verbose_name='опубликовано', default=True)
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='дата добавления')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'изделие'
        verbose_name_plural = 'изделия'

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)
        compress_product_image(
            directory=settings.MEDIA_ROOT,
            required_quality=self.PHOTO_CUALITY,
            time_to_compress=self.TIME_TO_COMPRESS
        )

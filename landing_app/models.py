from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='название изделия')
    description = models.TextField(verbose_name='описание')
    price = models.FloatField(verbose_name='цена')
    image = models.ImageField(verbose_name='фото', upload_to='')
    is_published = models.BooleanField(verbose_name='опубликовано', default=True)
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='дата добавления')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'изделие'
        verbose_name_plural = 'изделия'

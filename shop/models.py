from django.db import models
from django.urls import reverse


class Category(models.Model):
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, db_index=True)
    img = models.ImageField(upload_to='category/%Y/%m/%d', blank=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myshop:product_list_by_category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='products',
                                 on_delete=models.CASCADE)

    name = models.CharField(max_length=150, db_index=True)  # Наименование
    slug = models.SlugField(max_length=150, db_index=True, unique=True)

    image_1 = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)   # Изображение
    image_2 = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)   # Изображение
    image_3 = models.ImageField(upload_to='product/%Y/%m/%d', blank=True)   # Изображение

    description = models.TextField(max_length=1000, blank=True)  # Описание
    specifications = models.JSONField()     # Характеристики

    price = models.DecimalField(max_digits=10, decimal_places=2)    # Цена
    available = models.BooleanField(default=True)   # В наличии
    hot = models.BooleanField(default=False)    # Популярный
    discounted = models.BooleanField(default=False)  # Со скидкой
    markdown = models.BooleanField(default=False)   # Уцененнный

    created = models.DateTimeField(auto_now_add=True)   # Создан
    updated = models.DateTimeField(auto_now=True)   # Обновлен

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('myshop:product_detail', args=[self.id, self.slug])


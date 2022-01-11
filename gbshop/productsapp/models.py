from django.db import models

class ProductCategory(models.Model):
    name = models.CharField(
        verbose_name='Категория',
        max_length=64,
        unique=True,
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name='Товар',
        max_length=128,
    )
    image = models.ImageField(
        upload_to='products_images',
        blank=True,
    )
    short_desc = models.CharField(
        verbose_name='Краткое описание',
        max_length=60,
        blank=True,
    )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
    )
    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=8,
        decimal_places=2,
        default=0,
    )
    quantity = models.PositiveIntegerField(
        verbose_name='Количество на остатке',
        default=0,
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} ({self.category.name})'
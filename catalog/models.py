from django.db import models

class Catalog(models.Model):
    product = models.CharField(
        max_length=30, verbose_name="Продукт", help_text="Введите название продукта")
    category = models.ForeignKey('Catalog',
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию продукта",
        null=True,
        blank=True,
        related_name='catalogs')


    class Meta:
        verbose_name = "Каталог"
        verbose_name_plural = "Каталоги"
        ordering = ["category"]

    def __str__(self):
        return self.product


class Product(models.Model):
    product = models.CharField(
        max_length=30,
        verbose_name="Название продукта",
        help_text="Введите название продукта",
    )
    descriptions = models.TextField(
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
    )
    image = models.ImageField(upload_to='catalog/images', blank=True, null=True, verbose_name='Загрузите изображение')
    category = models.CharField(
        max_length=30,
        verbose_name="Название категории",
        help_text="Введите название категории",
        null = True
    )
    price = models.IntegerField(verbose_name='Введите цену продукта',null=True, help_text='Цена продукта')
    created_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата добавления')
    updated_at = models.DateTimeField(blank=True, null=True, verbose_name='Дата последнего изменения')


    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.product


class Category(models.Model):
    category = models.CharField(
        max_length=30,
        verbose_name="Название категории",
        help_text="Введите название категории",
    )
    descriptions = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категория"

    def __str__(self):
        return self.category

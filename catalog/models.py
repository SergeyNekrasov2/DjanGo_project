from django.db import models

class Category(models.Model):
    objects = None
    name = models.CharField(max_length=150, verbose_name='Наименование',null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Product(models.Model):
    objects = None
    names = models.CharField(max_length=150, verbose_name='Наименование',null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='картинки')
    category = models.CharField(max_length=150, verbose_name='Категория', null=True)
    group = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products',null=True)
    price = models.IntegerField()
    created_at = models.DateField(auto_now_add=True,null=True)
    updated_at = models.DateField(auto_now_add=True,null=True)
    views_counter = models.PositiveIntegerField(verbose_name='Счетчик просмотров', help_text='Укажите количество просмотров', default=0)
    status_publication = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.names}'

    class Meta:
        verbose_name = 'Имя продукта'
        verbose_name_plural = 'Имена продуктов'
        ordering = ['names']
        permissions = [
            ('can_unpublish_product', 'can unpublish product'),
        ]
# class Catalog(models.Model):
#     name = models.CharField(
#         max_length=30, verbose_name="Продукт", help_text="Введите название продукта"
#     )
#     category = models.CharField(
#         verbose_name="Категория",
#         help_text="Введите категорию продукта",
#         null=True,
#         blank=True,
#     )
#
#     class Meta:
#         verbose_name = "Каталог"
#         verbose_name_plural = "Каталоги"
#         ordering = ["category"]
#
#     def __str__(self):
#         return self.name
#
#
# class Product(models.Model):
#     names = models.CharField(
#         max_length=30,
#         verbose_name="Название продукта",
#         help_text="Введите название продукта",
#     )
#     descriptions = models.TextField(
#         verbose_name="Описание продукта",
#         help_text="Введите описание продукта",
#         blank=True,
#         null=True,
#     )
#     image = models.ImageField(
#         upload_to="catalog/images",
#         blank=True,
#         null=True,
#         verbose_name="Загрузите изображение",
#     )
#     group = models.ForeignKey(
#         "category",
#         on_delete=models.CASCADE,
#         max_length=30,
#         verbose_name="Название категории",
#         help_text="Введите название категории",
#         null=True,
#         blank=True,
#         related_name='category'
#     )
#     price = models.IntegerField(
#         verbose_name="Введите цену продукта", null=True, help_text="Цена продукта"
#     )
#     created_at = models.DateTimeField(
#         blank=True, null=True, verbose_name="Дата добавления"
#     )
#     updated_at = models.DateTimeField(
#         blank=True, null=True, verbose_name="Дата последнего изменения"
#     )
#
#     class Meta:
#         verbose_name = "Продукт"
#         verbose_name_plural = "Продукты"
#
#     def __str__(self):
#         return self.names
#
#
# class Category(models.Model):
#     name = models.CharField(
#         max_length=30,
#         verbose_name="Название категории",
#         help_text="Введите название категории",
#     )
#     descriptions = models.TextField(
#         verbose_name="Описание категории",
#         help_text="Введите описание категории",
#         blank=True,
#         null=True,
#     )
#
#     class Meta:
#         verbose_name = "Категория"
#         verbose_name_plural = "Категория"
#
#     def __str__(self):
#         return self.name

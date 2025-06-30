from django.db import models
from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование',null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Product(models.Model):

    objects = None
    names = models.CharField(max_length=50, unique=True,verbose_name='Наименование',null=True)
    description = models.TextField(null=True)
    image = models.ImageField(upload_to='images/catalog/', blank=True, null=True, verbose_name='картинки')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, max_length=50, verbose_name='Категория', null=True,related_name='category')
    # group = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products',null=True)
    price = models.IntegerField(null=True)
    created_at = models.DateField(auto_now_add=True,null=True)
    updated_at = models.DateField(auto_now_add=True,null=True)
    views_counter = models.PositiveIntegerField(verbose_name='Счетчик просмотров', help_text='Укажите количество просмотров', default=0)
    published = models.BooleanField(default=False, verbose_name='Признак публикации')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Владелец карточки', blank=True, null=True)
    # status_publication = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.names}'

    class Meta:
        verbose_name = 'Имя продукта'
        verbose_name_plural = 'Имена продуктов'
        ordering = ['names']
        permissions = [
            ('can_unpublish_product', 'Can unpublish product'),
            ('can_delete_product', 'Can delete product'),
        ]


from django.db import models

# class Catalog(models.Model):
#     first_name = models.CharField(max_length=150, verbose_name="Имя")
#     last_name = models.CharField(max_length=150, verbose_name_plural="Имя")
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
#
#     class Meta:
#         verbose_name = ''
#         verbose_name_plural = ''
#         ordering = ['last_name']
#         db_table = 'custom_table_name'
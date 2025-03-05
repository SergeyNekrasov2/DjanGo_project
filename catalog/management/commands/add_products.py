from django.core.management.base import BaseCommand
from django.core.management import call_command

from catalog.models import Category, Product

class Command(BaseCommand):

    help = 'Add products to the database'

    def handle(self, *args, **kwargs):

        Category.objects.all().delete()
        Product.objects.all().delete()


        call_command('loaddata', 'catalog_fixture.json')
        self.stdout.write(self.style.SUCCESS('Успех успешный'))

        category1, _ = Category.objects.get_or_create(name='Фрукты', description='Сладкие, вкусные', )
        category2, _ = Category.objects.get_or_create(name='Овощи', description='Спелые, полезные',)

        product1 = [{'names': 'Яблоки', 'description': 'Сладкие,вкусные', 'category': category1, 'price': 120}, ]
        product3 = [{'names': 'Огурцы', 'description': 'Зеленые,Крупные', 'category': category2, 'price': 80},]

        for prod_data in product1:
            prod, created = Product.objects.get_or_create(**prod_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'К успеху пришел ты: {prod.names}'))
            else:
                self.stdout.write(self.style.WARNING(f'Есть уже тут: {prod.names}'))

        for prod_data in product3:
            prod, created = Product.objects.get_or_create(**prod_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'К успеху пришел ты: {prod.names}'))
            else:
                self.stdout.write(self.style.WARNING(f'Есть уже тут: {prod.names}'))
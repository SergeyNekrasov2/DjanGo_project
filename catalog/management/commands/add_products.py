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


        category3, _ = Category.objects.get_or_create(name='Овощи', description='Спелые, полезные',)

        product3 = [{'names': 'Огурцы', 'description': 'Зеленые,Крупные', 'category': category3, 'price': 80},
                    {'names': 'Томаты', 'description': 'Красные,сливовые', 'category': category3, 'price': 180},]

        for prod_data in product3:
            prod, created = Product.objects.get_or_create(**prod_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'К успеху пришел ты: {prod.names}'))
            else:
                self.stdout.write(self.style.WARNING(f'Есть уже тут: {prod.names}'))
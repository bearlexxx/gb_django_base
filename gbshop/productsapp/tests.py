from django.test import TestCase
from django.test.client import Client
from django.core.management import call_command

from productsapp.models import ProductCategory, Product


class TestProductsappSmoke(TestCase):
    def setUp(self) -> None:
        call_command('flush', '--noinput')
        call_command('loaddata', 'test_db.json')
        self.client = Client()

    def test_productsapp_urls(self):

        for category in ProductCategory.objects.all():
            response = self.client.get(f'/products/category/{category.pk}/')
            self.assertEqual(response.status_code, 200)

        for product in Product.objects.all():
            response = self.client.get(f'/products/product/{product.pk}/')
            self.assertEqual(response.status_code, 200)

    def tearDown(self):
        call_command('sqlsequencereset', 'mainapp', 'authapp', 'ordersapp', 'basketapp')


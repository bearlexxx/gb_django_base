# Generated by Django 4.0 on 2022-01-03 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productsapp', '0002_product'),
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='количество')),
                ('add_datetime', models.DateTimeField(auto_now_add=True, verbose_name='время')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productsapp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='basket', to='authapp.shopuser')),
            ],
        ),
    ]

# Generated by Django 4.1.1 on 2022-09-28 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0003_alter_pizza_pizza_thin_large_pic_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='main_ingredients_can_remove',
            field=models.ManyToManyField(blank=True, related_name='main_can_remove', to='pizza.pizzaingredient', verbose_name='Основные ингредиенты, можно убрать'),
        ),
    ]

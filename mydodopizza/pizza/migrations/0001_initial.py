# Generated by Django 4.1.1 on 2022-09-28 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaIngredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название ингредиента')),
                ('cost', models.IntegerField(verbose_name='Стоимость маленькой пиццы')),
                ('inrg_picture', models.ImageField(null=True, upload_to='ingredient/', verbose_name='Фото ингредиента')),
            ],
            options={
                'verbose_name': 'Ингредиенты',
                'verbose_name_plural': 'Ингредиенты',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название пиццы')),
                ('cost_small_pizza', models.IntegerField(verbose_name='Стоимость маленькой пиццы')),
                ('cost_medium_pizza', models.IntegerField(verbose_name='Стоимость средней пиццы')),
                ('cost_large_pizza', models.IntegerField(verbose_name='Стоимость большой пиццы')),
                ('main_picture', models.ImageField(null=True, upload_to='pizza/', verbose_name='Фото на главной странице')),
                ('pizza_trad_small_pic', models.ImageField(upload_to='pizza/', verbose_name='Фото маленький круг традиционное тесто')),
                ('pizza_trad_medium_pic', models.ImageField(upload_to='pizza/', verbose_name='Фото средний круг традиционное тесто')),
                ('pizza_trad_large_pic', models.ImageField(upload_to='pizza/', verbose_name='Фото большой круг традиционное тесто')),
                ('pizza_thin_medium_pic', models.ImageField(upload_to='pizza/', verbose_name='Фото средний круг тонкое тесто')),
                ('pizza_thin_large_pic', models.ImageField(upload_to='pizza/', verbose_name='Фото большой круг тонкое тесто')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовать на сайте')),
                ('additional_ingredients', models.ManyToManyField(related_name='additional_ing', to='pizza.pizzaingredient', verbose_name='Дополнительные ингредиенты')),
                ('ingredients', models.ManyToManyField(to='pizza.pizzaingredient')),
                ('main_ingredients', models.ManyToManyField(related_name='main_ing', to='pizza.pizzaingredient', verbose_name='Основные ингредиенты')),
                ('main_ingredients_can_remove', models.ManyToManyField(related_name='main_can_remove', to='pizza.pizzaingredient', verbose_name='Основные ингредиенты, можно убрать')),
            ],
            options={
                'verbose_name': 'Каталог пиццы',
                'verbose_name_plural': 'Каталог пиццы',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='GroupIngredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя группы ингредиентов')),
                ('group', models.CharField(choices=[('main_ingredients', 'Основные ингредиенты'), ('main_ingredients_can_remove', 'Основные ингредиенты, можно убрать'), ('additional_ingredients', 'Дополнительные ингредиенты')], max_length=100)),
                ('ingredients', models.ManyToManyField(to='pizza.pizzaingredient')),
                ('pizza', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='pizza.pizza', verbose_name='Пицца')),
            ],
        ),
    ]

from django.db import models


# class Category(models.Model):
#     cat_name = models.CharField(max_length=100, null=False, verbose_name='Категория')
#
#     def __str__(self):
#         return self.cat_name
#
#     class Meta:
#         verbose_name = 'Категории'
#         verbose_name_plural = 'Категории'
#         ordering = ['id', ]

#
# class PizzaIngredient(models.Model):
#
#     name = models.CharField(max_length=100, null=False, verbose_name='Название ингредиента')
#     cost = models.IntegerField(null=False, verbose_name='Стоимость маленькой пиццы')
#     inrg_picture = models.ImageField(upload_to='ingredient/', null=True, verbose_name='Фото ингредиента')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Ингредиенты'
#         verbose_name_plural = 'Ингредиенты'
#         ordering = ['id', ]
#
#
# class GroupIngredients(models.Model):
#
#     GROUPS = (
#         ('main_ingredients', 'Основные ингредиенты'),
#         ('main_ingredients_can_remove', 'Основные ингредиенты, можно убрать'),
#         ('additional_ingredients', 'Дополнительные ингредиенты'),
#     )
#
#     name = models.CharField(max_length=100, null=False, verbose_name='Имя группы ингредиентов')
#     group = models.CharField(max_length=100, choices=GROUPS)
#     pizza = models.ForeignKey('Pizza', on_delete=models.PROTECT, null=True, verbose_name='Пицца')
#     ingredients = models.ManyToManyField('PizzaIngredient', related_name='test')
# #
# #
# # # class MainIngredientsCanRemove(models.Model):
# # #     ingredient = models.ManyToManyField('PizzaIngredient')
# # #
# # #
# # # class AdditionalIngredients(models.Model):
# # #     ingredient = models.ManyToManyField('PizzaIngredient')
#
#
# class Pizza(models.Model):
#
#     name = models.CharField(max_length=100, null=False, verbose_name='Название пиццы')
#
#     category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория товара')
#     # ingredients = models.ManyToManyField('PizzaIngredient')
#     # main_ingredients = models.ForeignKey(
#     #     'PizzaIngredient', on_delete=models.PROTECT, null=True, verbose_name='Основные ингредиенты'
#     # )
#     # main_ingredients_can_remove = models.ForeignKey(
#     #     'PizzaIngredient', on_delete=models.PROTECT, null=True, verbose_name='Основные ингредиенты, можно убрать'
#     # )
#     # additional_ingredients = models.ForeignKey(
#     #     'PizzaIngredient', on_delete=models.PROTECT, null=True, verbose_name='Дополнительные ингредиенты'
#     # )
#
#     def main_ingredients(self):
#         # return GroupIngredients.objects.filter(pizza=self.id)
#         return GroupIngredients.objects.all()
#
#     cost_small_pizza = models.IntegerField(null=False, verbose_name='Стоимость маленькой пиццы')
#     cost_medium_pizza = models.IntegerField(null=False, verbose_name='Стоимость средней пиццы')
#     cost_large_pizza = models.IntegerField(null=False, verbose_name='Стоимость большой пиццы')
#
#     main_picture = models.ImageField(upload_to='pizza/', verbose_name='Фото на главной странице', null=True)
#     pizza_trad_small_pic = models.ImageField(upload_to='pizza/', verbose_name='Фото маленький круг традиционное тесто')
#     pizza_trad_medium_pic = models.ImageField(upload_to='pizza/', verbose_name='Фото средний круг традиционное тесто')
#     pizza_trad_large_pic = models.ImageField(upload_to='pizza/', verbose_name='Фото большой круг традиционное тесто')
#     pizza_thin_medium_pic = models.ImageField(upload_to='pizza/', verbose_name='Фото средний круг тонкое тесто')
#     pizza_thin_large_pic = models.ImageField(upload_to='pizza/', verbose_name='Фото большой круг тонкое тесто')
#
#     is_published = models.BooleanField(default=True, verbose_name='Опубликовать на сайте')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Каталог пиццы'
#         verbose_name_plural = 'Каталог пиццы'
#         ordering = ['id', ]




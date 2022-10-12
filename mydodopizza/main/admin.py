from django.contrib import admin

from .models import *


# class PizzaAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'cost_small_pizza', 'cost_medium_pizza', 'cost_large_pizza', 'pizza_trad_medium_pic', 'is_published')
#     list_display_links = ('id', 'name')
#     search_fields = ('name',)
#     list_filter = ('is_published',)
#     list_editable = ('cost_small_pizza', 'cost_medium_pizza', 'cost_large_pizza', 'is_published')
#
#
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('cat_name', )
#
#
# class PizzaIngredientAdmin(admin.ModelAdmin):
#     list_display = ('name', 'cost', 'inrg_picture')
#
#
# class GroupIngredientsAdmin(admin.ModelAdmin):
#     list_display = ('name', )
#
# admin.site.register(Category, CategoryAdmin)


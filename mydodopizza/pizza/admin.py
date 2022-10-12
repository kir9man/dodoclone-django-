from django.contrib import admin
from django.contrib.admin.views.main import ChangeList

from .models import *


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cost_small_pizza', 'cost_medium_pizza', 'cost_large_pizza', 'pizza_trad_medium_pic', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('is_published',)
    list_editable = ('cost_small_pizza', 'cost_medium_pizza', 'cost_large_pizza', 'is_published')


class PizzaIngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'inrg_picture')


class GroupIngredientsAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(Pizza, PizzaAdmin)
admin.site.register(PizzaIngredient, PizzaIngredientAdmin)
admin.site.register(GroupIngredients, GroupIngredientsAdmin)

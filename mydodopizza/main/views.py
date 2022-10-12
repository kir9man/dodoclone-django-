from django.shortcuts import render

from .models import *
from pizza.models import *


def make_ingredients_list(queryset: list[Pizza]) -> list[str]:
    ingredients_list = []
    for pizza in queryset:
        main_igr = [ingredient.name for ingredient in pizza.main_ingredients.all()]
        main_igr_can_remove = [ingredient.name for ingredient in pizza.main_ingredients_can_remove.all()]
        main_igr.extend(main_igr_can_remove)
        ingredients_list.append(', '.join(main_igr).capitalize())
    return ingredients_list


def main(request):

    pizza = Pizza.objects.filter(is_published=True)

    # pizza |= make_ingredients_list(pizza)

    return render(request, 'main/main.html', {
        'pizza': pizza,
        'ingredients_list': make_ingredients_list(pizza),
    })
    # return render(request, 'main/main.html', {'pizza': list(range(8))})

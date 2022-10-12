from django import forms
from .models import Pizza


# class IngredientChangeListForm(forms.ModelForm):
#
#     # here we only need to define the field we want to be editable
#     main_ingredients = forms.ModelMultipleChoiceField(queryset=Pizza.objects.all(), required=False)
#     main_ingredients_can_remove = forms.ModelMultipleChoiceField(queryset=Pizza.objects.all(), required=False)
#     additional_ingredients = forms.ModelMultipleChoiceField(queryset=Pizza.objects.all(), required=False)
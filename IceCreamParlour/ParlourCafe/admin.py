from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(FlavourModel)
admin.site.register(IngredientModel)
admin.site.register(AllergyModel)
admin.site.register(FlavourSuggestionModel)
admin.site.register(CartModel)
admin.site.register(UserDb)

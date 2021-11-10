from django.contrib import admin
from django.db.models import fields
from .models import Ingredients, MenuItem, RecipeRequirements
# Register your models here.

class IngredientsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    fields = ('name','unit','quantity','unit_price','slug')

admin.site.register(Ingredients,IngredientsAdmin)

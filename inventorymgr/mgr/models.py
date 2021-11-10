from django.db import models
from django.db.models.base import Model
from django.utils.text import slugify

# Create your models here.
class Ingredients(models.Model):
    """ 
    Model to track inventory of ingredients
    """
    slug = models.SlugField(unique=True,max_length=255)
    name = models.CharField(verbose_name='Name',null=False,blank=False,max_length=255)
    unit = models.CharField(verbose_name='Unit',max_length=5)
    quantity = models.IntegerField(default=0)
    unit_price = models.FloatField(default=0.0)

    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        return ''

class MenuItem(models.Model):
    """
    Model to track menu items
    """
    menu_item = models.CharField(max_length=255)
    price = models.FloatField(max_length=5)
    slug = models.SlugField(unique=True,max_length=255)

    def __str__(self) -> str:
        return self.name
    
    def save(self,*args):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(self).save()
    
class RecipeRequirements(models.Model):
    """
    Model for tracking recipe requirements for recipes
    """
    descp = models.CharField(blank=True,max_length=255)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE,max_length=255)
    Ingredient = models.ForeignKey(Ingredients,on_delete=models.CASCADE,max_length=255)
    quantity = models.FloatField(default=0.0, blank=False,null=False)

    def __str__(self) -> str:
        return self.descp if self.descp is not None else 'Recipe requirement'
    

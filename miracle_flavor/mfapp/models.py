from django.db import models

# Create your models here.

class Aboutus(models.Model):
    com_name = models.CharField(max_length=100)
    com_details = models.TextField()
    
    
class Product(models.Model):
    product_name = models.CharField(max_length=100)
    product_image = models.ImageField(upload_to='products')
    
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_image = models.ImageField(upload_to='recipes')
    recipe_making = models.TextField()
    
    
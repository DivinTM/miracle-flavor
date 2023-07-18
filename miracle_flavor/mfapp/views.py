from django.shortcuts import render
from django.http import HttpResponse

from .models import Aboutus,Product,Recipe

# Create your views here.
def index(resquest):
    return render(resquest,'index.html')

def about(resquest):
    dict_about={
        'abt' : Aboutus.objects.all()
    }
    return render(resquest,'about.html',dict_about)

def product(resquest):
    dict_prod = {
        'products': Product.objects.all()
    }
    return render(resquest,'product.html',dict_prod)

def media(resquest):
    return render(resquest,'media.html')

def recipe(resquest):
    dict_rec = {
        'recipe' : Recipe.objects.all()
        }
    return render(resquest,'recipe.html',dict_rec)

def contact(resquest):
    return render(resquest,'contact.html')
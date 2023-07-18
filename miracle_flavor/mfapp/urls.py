from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.index,name='home'),
    path('about/', views.about,name='about'),
    path('product/', views.product,name='product'),
    path('media/', views.media,name='media'),
    path('recipe/', views.recipe,name='recipe'),
    path('contact/', views.contact,name='contact'),
]
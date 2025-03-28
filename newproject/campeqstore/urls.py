from django.urls import path
from .views import hello_world, about_shop

urlpatterns = [
    path('', hello_world, name='hello_world'),
    path('about/', about_shop, name = 'about_shop'),
    #path('author/', ),
]
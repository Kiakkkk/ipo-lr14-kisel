from django.urls import path
from .views import index, about_shop, author, specialties, spec_id

urlpatterns = [
    path('', index, name='index'),
    path('about/', about_shop, name = 'about_shop'),
    path('author/', author, name = 'author'),
    path('spec/', specialties),
    path('spec/<int:id>/', spec_id),
]
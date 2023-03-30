from django.urls import path
from .views import Categoria, Animals

from django.urls import path
from .views import index, Animals, Categoria

urlpatterns = [
    path('index.html', index, name='index'),
    path('', Animals, name='Animals'),
    path('', Categoria, name='Categoria'),
]
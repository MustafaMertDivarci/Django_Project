
# Bu sayfayı ben oluşturdum ana dosyalardan django_project/urls.py kopyala yapıştırır ile.

from django.urls import path
from . import views

urlpatterns = [
    
    # path kendi içerisinde iki parametre alır:
    # path(route,view,opt(kısayol ismi)) route->yönü verir

    path('', views.index, name="index"),

   
]
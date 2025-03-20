"""
URL configuration for projectDjango1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
#ici jimporte tout les views dans meszrticles
from mesarticles.views import * # jimporte toute mes veues dand le fichier views


from django.urls import path, include
from rest_framework.routers import DefaultRouter

from wamybank.views import connexion_bank


route = DefaultRouter()
route.register(r'etudiant', MaVueEtudiantSerialise)
route.register(r'universites',MaVueUniversiteSerialise)
route.register(r'employes',MaVueEmployeSerialise)


urlpatterns = [
   
    
    path('',connexion , name='connexion'), # 1er parge du site
    path('',connexion_bank , name='connexion_bank'), # 1er parge du site
    
    
    path('admin/', admin.site.urls, name='admin'),
    # pour lier toutes les route (urls de mon application mesarticles)
    path('art/', include("mesarticles.urls")),   # inclure lien de nom qppli nmsarticles
    path('bank/', include("wamybank.urls")),  
    path('api/', include(route.urls)),
]
 




urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



'''
pour mon fichier css
<!--link rel="stylesheet" type="text/css" href="{% static 'styleConnexion.css' %}"-->
 <!-- aller a la page connexion.html 
         <a href="{% url 'accueil' %}"> Retour a laccueil </a> -->

'''
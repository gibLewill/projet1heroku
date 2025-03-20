

from django.db import router
from django.urls import include, path

from wamybank.views import *
 




urlpatterns = [
    path('operations', operations, name='operations'),
    path('depot', depot, name='depot'),
    path('retrait', retrait, name='retrait'),
    path('virement', virement, name='virement'),
    path('historique', historique, name='historique'),
    path('listing', listing, name='listing'),
    
    path('gestion_compte', gestion_compte, name='gestion_compte'),
    path('gestion_client', gestion_client, name='gestion_client'),
    
    path('creer_client', creer_client, name='creer_client'),
    path('creer_compte', creer_compte, name='creer_compte'),
    path('creer_compte_epargne', creer_compte_epargne, name='creer_compte_epargne'),
    
    path('liste_client', liste_client, name='liste_client'),
    path('liste_compteC', liste_compteC, name='liste_compteC'),
    path('liste_compteE', liste_compteE, name='liste_compteE'),
    
    #path('liste_articles_Cat/<int:id>', liste_articles_Cat, name='liste_articles_Cat'), # urls dune routre dynamique
    #path('connexion_bank', connexion_bank, name='connexion_bank'),
]
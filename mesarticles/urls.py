'''
pour les Urls de mon application mesAticles
et puis les lie avec le fichier Url principale

par le 
parth('',include(nomAppli.urls))
ici  parth('',include(mesarticles.urls))
'''

from django.db import router
from django.urls import include, path
#ici jimporte tout les views dans meszrticles
import mesarticles
from mesarticles.views import * # jimporte toute mes veues dand le fichier views

'''
     ici  ( urlpatterns ) je met tous les urls des mes vues  
     ces  vues appele home son chemin est http://127.0.0.1:8000/accueil
    
     entre ('' et name) sont  ecrites le nom du fichier htmt et au milieu le nom de la fonction 
     qui traite le fichier html .ces noms peuvent etre identique
     
'''  
 




urlpatterns = [
    path('accueil', accueil, name='accueil'),
    path('logout/',deconnexion, name='logout'),
    path('inscription',register, name='inscription'),

    
    

    path('create_article',create_article, name='create_article'),
    path('liste_article', liste_article, name='liste_article'),
    path('liste_articles_Cat/<int:id>', liste_articles_Cat, name='liste_articles_Cat'), # urls dune routre dynamique
    path('supprimer_article/<int:id>',supprimer_article , name='supprimer_article'), # urls dune routre dynamique
    path('modifier_article/<int:id>',modifier_article , name='modifier_article'), # urls dune routre dynamique
    path('detail_article/<int:id>',detail_article , name='detail_article'),
    path('like_commentaire/<int:id>',like_commentaire , name='like_commentaire'),
    
    
    path('create_categorie',create_categorie, name='create_categorie'),
    path('liste_categorie', liste_categorie, name='liste_categorie'),
    
    path('create_etudiant', create_etudiant, name='create_etudiant'),
    path('liste_Etudiant', liste_Etudiant, name='liste_Etudiant'),
    path('detailEtudiant/<int:id>', detailEtudiant , name='detailEtudiant'),
    path('listeUniver_Etu/<int:id>', listeUniver_Etu , name='listeUniver_Etu'),
    
   
    
    path('create_universite',create_universite, name='create_universite'),
    path('liste_Universite',liste_Universite, name='liste_Universite'),
    path('listeEtu_Univer/<int:id>',listeEtu_Univer, name='listeEtu_Univer'), # urls dune routre dynamique
    
    path('liste_Personne', liste_Personne , name='liste_Personne'),
    path('create_contact', create_contact, name='create_contact'),

    path('formulaire_incription', formulaire_incription , name='formulaire_incription'),


# ajoute des route pour lauthantification
#path('register', register, name='register');
    
]
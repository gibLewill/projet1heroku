from django.test import TestCase
from django.urls import resolve

from mesarticles.models import *


class MesarticlesTest (TestCase):
    def test_creation_categorie(self):
        print(' debut test 1')
        maCat = Categorie.objects.create(nom='maCatTEST')
        self.assertIsInstance(maCat,Categorie)
        print(' fin test 1')
        
        
    def test_route_dynamique_commentaire (self):
        print(' debut test ma_route_dynamique')
        
        
        # mon model pour tester la route
        monAr = Article.objects.create(titre = 'articleTest')
        print(monAr, ' cree')
        #construire lurl de la route de larti
        url = reversed('detail_article',argr=[monAr.id])
        
        print(url , 'ur trouvee')
        # tester la reponse de la vue
        reponseVue = self.client.get(url)
        
        # verifier si la reponse est ok
        self.assertEqual(reponseVue.status_code, 200)
        print(reponseVue,' vue ok')
        #relie a la vue associe
        ma_vue_associe = resolve(url).func
        
        #verifier si la vue bien celle attendue
        self.assertEqual(ma_vue_associe.__name__,'detail_article')
        print(ma_vue_associe,' existe belle est bien')
        
        
        
        
    
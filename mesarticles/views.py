from urllib import request
from django.shortcuts import get_object_or_404, redirect, render

from django.core.paginator import Paginator


from mesarticles.form import *
from mesarticles.models import Article,Etudiant,Universite
from django.db.models import *

from mesarticles.serialisateur import EtudiantSerialiser, UniversiteSerialiser, EmployeSerialiser

# import pour API
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

#from rest_framework.permissions import
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Etape 1 Creation des vues de connexion

# on creation dun nouvel utilisateur
def register (req):
   print('Entree 1')
   if req.method == 'POST':
      print('Entree post')
      # on creer le formulaire
      formulaire = UserCreationForm(req.POST)
      print(' form post donne')
      if formulaire.is_valid():
         formulaire.save()
         nomCreer = req.POST['username']
         print(nomCreer)
         return render(req, 'confirmation.html', {'nomCreer':nomCreer})
   else : # si ne post nest pas declancher
      # on cree le formulaire vide utilisateur
      print(' form vide donne')
      formulaire = UserCreationForm()
   return render (req, 'inscription.html', {'formulaire':formulaire})

# il se  connecte biensur sil existe
def connexion(req):
   message = ''
   # pour se faire on recupere ses informations
   if req.method =='POST':
      nomUtilisateur = req.POST['username']
      motdePass = req.POST['password']
      user = authenticate(req, username = nomUtilisateur, password=motdePass)
      if user is not None: # si user existe alor on le connecte
         login(req,user)
         return redirect ('accueil')
      else:
         message = 'Mot de Passe ou Login incorrect'
         
   return render (req,'connexion.html' ,{'message':message}) 


# page pour deconnecte un utilisateur connecte
def deconnexion (req):
   print('')
   print(req.user.username)
   logout(req)
   print('est deconnecte')
   return redirect('connexion')  
   


# Create your views here.
# nous permettre de creer nos vue pour gerer des templates

def accueil(requette):
   categories  = Categorie.objects.all() # lobjet articles contient tous nos articles
   univers = Universite.objects.all()
   
   print('')
   print(requette.user.username)
   print('est connecte')
   
   return render (requette,'accueil.html', {'categories': categories, 'univers':univers} )
   
   return render(requette,'accueil.html', {'x':5})
    # le render prend mq reauette en parm et ma parge html et mon dict de donnes(x) wui seront donc zfficher dans le mon html  

'''
+++++++++++++++++++ traintement sur les Articles  +++++++++++++++++++++++++++++

'''
# 2)  vue pour les articles
def create_article (request):
   formulaire = ArticleForm()
   if request.method == 'POST':
      # on cree un objet formulaire pour lui passer notre formulaire
       formulaire = ArticleForm(request.POST)
       if formulaire.is_valid():
          formulaire.save()
          message = 'Enregistrement effectue avec success !'
          return render(request,'create_article.html', {'message':message})
       else :
          formulaire = ArticleForm()
   return render(request,'create_article.html', {'formulaire':formulaire})

def supprimer_article(req,id):
   art = Article.objects.get(id=id)
   art.delete()
   message = art.titre+" Supprime avec Success"
   articles  = Article.objects.all() # lobjet articles contient tous nos articles
   taille = len(articles)
   return render (req,'supprimer_article.html', {'articles': articles, 'taille': taille, 'message':message })


def modifier_article(req,id):
   # on recupere id de l objet a modifier
   art = Article.objects.get(id=id)
   formulaire = ArticleForm(instance=art)
   if req.method=='POST':
      formulaire = ArticleForm(req.POST,instance=art)
      if formulaire.is_valid():
          formulaire.save()
          message = 'Modification  effectue avec success !'
          return render(request,'liste_article.html', {'message':message})
      else :
          formulaire = ArticleForm(instance=art)      
   return render(request,'modifier_article.html', {'formulaire':formulaire})
   


   
def liste_article (req):
   articles  = Article.objects.all() # lobjet articles contient tous nos articles
   taille = len(articles)

   # creation de la pargination (un parginateur)
   paginateur = Paginator(articles,5) # 2 articles par page
   # Récupérer la page actuelle
   page_actuelle = req.GET.get('page')
   # Récupérer les données pour la page actuelle
   donnees_page_actuelle = paginateur.get_page(page_actuelle)

   return render (req,'liste_article.html', {'articles': donnees_page_actuelle, 'taille': taille})
   


#liste des article dune categorie en utilisant class_set.all()
# pour le foreignkey cote article
def liste_articles_Cat(req,id):
   ma_cat = Categorie.objects.get(id=id)
   mesArticles = ma_cat.article_set.all()
   taille = len(mesArticles)
   return render (req,'liste_articles_Cat.html', {'mesArticles':mesArticles , 'taille':taille, 'ma_cat':ma_cat})
'''
-- traintement sur les Commentaires  -------------

'''
# cest dans lafficharge de larticle en details quon donnera la possibilite a
# un utilisateur dajouter (creer) un commentaire

@login_required # access uniquement aux use connecte
def detail_article(request,id):
   article = get_object_or_404(Article,id=id)
   commentaires = article.commentaire_set.all()
   t = len(commentaires)
   formulaire = CommentaireForm()
   if request.method == 'POST':
      formulaire = CommentaireForm(request.POST)
      if formulaire.is_valid():
         commentaire = formulaire.save(commit=False)
         commentaire.article = article # specifier larticle
         commentaire.auteur = request.user
         commentaire.save()
      else :
         formulaire = CommentaireForm()
   return render(request, 'detail_article.html', {'article': article, 'commentaires': commentaires, 'formulaire': formulaire, 't':t})
  
@login_required
def like_commentaire (request,id):
   print('')
   commentaire = get_object_or_404(Commentaire, id=id)
   like1, created = like.objects.get_or_create(auteur=request.user, commentaire=commentaire)
   print(like1)
   if not created:
      like1.delete()
      print('if')
   return redirect ('detail_article', id=commentaire.article.id) 
     
'''
-- traintement sur les likes et favorie -------------

'''       
def favorie (request):
   pass
         


'''
-- traintement sur les  Categories -------------

'''
# 2)  vue pour les categories
def create_categorie (request):
   formulaire = CategorieForm()
   if request.method == 'POST':
       formulaire = CategorieForm(request.POST)
       if formulaire.is_valid():
          formulaire.save()
          message = 'Enregistrement effectue avec success !'
          return render(request,'create_categorie.html', {'message':message})
       else :
          formulaire = CategorieForm()
   
   return render(request,'create_categorie.html', {'formulaire':formulaire})


def liste_categorie (req):
   categories  = Categorie.objects.all() # lobjet articles contient tous nos articles
   taille = len(categories)
   return render (req,'liste_categorie.html', {'categories': categories, 'taille': taille})


'''
-- traintement sur les  Etudiants -------------

'''
def create_etudiant (request):
   formulaire = EtudiantForm()
   if request.method == 'POST':
       formulaire = EtudiantForm(request.POST)
       if formulaire.is_valid():
          formulaire.save()
          message = 'Enregistrement effectue avec success !'
          return render(request,'create_etudiant.html', {'message':message})
       else :
          print(' etudiant  mal remplir')
          message =' les informations saisies ne sont correct'
          formulaire = EtudiantForm()
          return render(request,'create_etudiant.html', {'message':message})
   
   return render(request,'create_etudiant.html', {'formulaire':formulaire})

def liste_Etudiant (req):
   # la requette
   etudiants = Etudiant.objects.all() 
   nombre_etudiant = len(etudiants)
   
   '''  
   les filtres simple 
   '''
  
   # liste des etudiants avec une taille > 150
   etudiantPlus150m = Etudiant.objects.filter(taille__gt=150)
   # liste des etudiants dont le nom commence par la lettre M
   etudiantLettreM = Etudiant.objects.filter(nom__istartswith='M')
   # liste des etudiants dont le nom commence par la lettre M et la taille >150
   etudiantLettreM_Plus150m = etudiantPlus150m.filter(nom__istartswith='M')
     
   '''  
   les filtres avec condition Q()
   '''
    # Trouver les livres qui sont soit écrits par un 
    # auteur spécifique soit coûtent moins de 20$
   # trouvons la liste des etudiants ( soit le mat comment par 14 soit un leur taille>170) le OR(|)
   etuMat14_taille170 = Etudiant.objects.filter(Q(matricule__istartswith='14') | Q(taille__gt=170))
   # trouvons la liste des etudiants dont le mat comment par 14 et la taille>170) le AND(&)
   etuMat14_et_taille170 = Etudiant.objects.filter(Q(matricule__istartswith='14') & Q(taille__gt=170))
   '''  
   les filtres et les tris
   '''
   # liste des etudiant classe par ordre alphabetique
   etu_classe = Etudiant.objects.all().order_by('nom')
   
   # les aggregations
   # le Count
   resultat = Etudiant.objects.aggregate(Count('nom'),Sum('taille'),Avg('taille'),Max('taille'),Min('taille'))
   

   
   return render (req, 'liste_Etudiant.html', {'LesEtudiants':etudiants,
                                               'nombre_etudiant':nombre_etudiant,
                                               'etudiantPlus150m':etudiantPlus150m,
                                               'etudiantLettreM':etudiantLettreM,
                                               'etudiantLettreM_Plus150m':etudiantLettreM_Plus150m,
                                               'etuMat14_taille170':etuMat14_taille170,
                                               'etuMat14_et_taille170':etuMat14_et_taille170,
                                               'etu_classe':etu_classe,
                                               'resultat':resultat, 
                                               
                                               })
                                               

def  detailEtudiant (req, id):
   etu = Etudiant.objects.get(id=id)  
   return render (req, 'detailEtudiant.html', {'id_etu':id, 'etu':etu})

#liste des etu dune univer
# avec le ManyToMany cote Universite
def  listeEtu_Univer (req, id):
   monUniversite = Universite.objects.get(id=id)
   mesEtudiants = monUniversite.etu.all()
   nbr = len(mesEtudiants)
   return render (req, 'listeEtu_Univer.html', {'univer':monUniversite, 'mesEtudiants':mesEtudiants, 'nbr':nbr})

#liste des Univerte dun etu
# avec le ManyToMany cote Universite0
def  listeUniver_Etu (req, id):
   monEtu = Etudiant.objects.get(id=id)
   sesUniversites = monEtu.universite_set.all()
   nbr = len(sesUniversites)
   return render (req, 'listeUniver_Etu.html', {'etu':monEtu, 'sesUniversites':sesUniversites, 'nbr':nbr})

'''
 code pour l api en effet la vue du serialiseur
'''
# ma class de model serialise
class MaVueEtudiantSerialise (viewsets.ModelViewSet,APIView):
   queryset = Etudiant.objects.all()
   serializer_class = EtudiantSerialiser
   # ces deux lignes represente la methode get
  # permission_classes = [IsAuthenticated] # cette ligne fait que la vue soit  accessible uniquement aux utilisateurs authentifiés
   
   
   
   
# traitement pour la suppression e maj
   def put (self,request,pk):
      etu = Etudiant.objects.get(pk=pk) # je recupere l etu
      serialisez = EtudiantSerialiser(etu, data=request.data) # jappelle le serialisateur sur mon objet
      if serialisez.is_Valid():
         serialisez.save()
         return Response (serialisez.data)
      return Response (serialisez.errors,status=status.HTTP_400_BAD_REQUEST)
   
    # methode de modification partiel
   def patch (self,request,pk):
      etu = Etudiant.objects.get(pk=pk) # je recupere l etu
      serialisez = EtudiantSerialiser(etu, data=request.data, partial=True) # jappelle le serialisateur sur mon objet
      if serialisez.is_Valid():
         serialisez.save()
         return Response (serialisez.data)
      return Response (serialisez.errors,status=status.HTTP_400_BAD_REQUEST)
   
   def delete (self,pk):
      etu = Etudiant.objects.get(pk=pk) # je recupere l etu a delete
      etu.delete()
      return Response (status=status.HTTP_204_NO_CONTENT)
   
      

      
   
# ma class Universite de model serialise
class MaVueUniversiteSerialise (viewsets.ModelViewSet):
   queryset = Universite.objects.all()
   serializer_class = UniversiteSerialiser
   
   
   
   


'''
-- traintement sur les  Universites -------------

'''
def create_universite (request):
   formulaire = UniversiteForm()
   if request.method == 'POST':
      # on cree un objet formulaire pour lui passer notre formulaire
       formulaire = UniversiteForm(request.POST)
       if formulaire.is_valid():
          formulaire.save()
          message = 'Enregistrement effectue avec success !'
          #return redirect ('liste_article')
          return render(request,'create_universite.html', {'message':message})
       else :
          formulaire = UniversiteForm()
   
   return render(request,'create_universite.html', {'formulaire':formulaire})

def liste_Universite (req):
   # la requette
   univers = Universite.objects.all()
   taille = len(univers)
   # un requette ManyToMany le ppefetch_related
   univers2 = Universite.objects.prefetch_related('etu').all()
   return render (req, 'liste_Universite.html', {'universites':univers, 'taille':taille})




'''
-- traintement sur les  exemples personnel du cours-------------

'''
# traitement de mon forumulaire dinscription\
   
def formulaire_incription (request):
   formulaire = Form_Inscription()
   print(' je suis dans formulaire inscription avant le if ')
   if request.method == 'POST':
      # on cree un objet formulaire pour lui passer notre formulaire
       print(' je suis dans formulaire inscription apres le if ')
       formulaire = Form_Inscription(request.POST)
       if formulaire.is_valid():
          print(' je suis dans formulaire inscription save ')
          #formulaire.save()
          message = 'Enregistrement effectue avec success !'
          #return redirect ('liste_article')
          return render(request,'formulaire_incription.html', {'message':message})
       else :
          formulaire = Form_Inscription()
   
   return render(request,'formulaire_incription.html', {'formulaire':formulaire})

def create_contact (request):
    formulaire = ContactForm() 
    print('CREATION DU FORMULAIRE')
    if request.method == 'POST':
       formulaire = ContactForm(request.POST)
       print('1ER DE VU')
       if formulaire.is_valid():
          print('ENREGISTRE AVEC SUCESS')
          return redirect('create_contact')
       else:
         print('3IEME DE VU')
         formulaire = ContactForm() 
         
    return render(request,'create_contact.html', {'formulaire':formulaire})
 
 
'''

++++++ traitement Personne 
 
'''
def create_personne (request):
   formulaire = PersonneForm()
   if request.method == 'POST':
       formulaire = PersonneForm(request.POST)
       if formulaire.is_valid():
          formulaire.save()
          message = 'Enregistrement effectue avec success !'
          return render(request,'create_personne.html', {'message':message})
       else :
          message =' les informations saisies ne sont correct'
          formulaire = PersonneForm()
          return render(request,'create_personne.html', {'message':message})
   
   return render(request,'create_personne.html', {'formulaire':formulaire})

def liste_Personne (req):
   # les requette simple
   personne = Personne.objects.all() 
   nbr = len(personne)
  # les requettes dans le OnetoOne+++++++++++++++
  # liste des pesonne qui vive a yaounde
   personneYde = Personne.objects.filter(adresse__ville='Yaounde')
   nbr1 = len(personneYde)
   
   personneAdr = Personne.objects.select_related('adresse').all()
   adresses = Adresse.objects.all() 
   nbr2 = len(adresses)
   
   # les filtres simple
   # les personne dont lage est < 30
   age = 30
   personneAge30 = Personne.objects.filter(age__gt=age)
   
   
   return render (req, 'liste_Personne.html', {
                                              'personne':personne,
                                               'nbr':nbr,
                                               'personneYde': personneYde, 
                                               'personneAdr':personneAdr,
                                               'nbr1':nbr1,
                                               'adresses':adresses,
                                               'nbr2':nbr2
                                               })

'''
 vue pour Employe
'''
class MaVueEmployeSerialise (viewsets.ModelViewSet,APIView):
   queryset = Employe.objects.all()
   serializer_class = EmployeSerialiser
'''
 class Command(BaseCommand):
    help = 'Générer des employés fictifs'

    def handle(self, *args, **kwargs):
        fake = Faker()
        for _ in range(10):  # Le nombre d'employés à générer
            Employe.objects.create(
                nom=fake.last_name(),
                prenom=fake.first_name(),
                email=f
 
 '''  

   
   
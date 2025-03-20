from datetime import date
from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User


# Create your models here.
# pour creer nos tables 


class Article(models.Model):
    # attributs qui deviennent des colones dans la bd
    titre = models.CharField(max_length=255)
    contenu = models.TextField()
    date_publication = models.DateField(auto_now_add=True)
    categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images_articles',blank=True, null=True)
    # like est une table tampon en Article et User (n,n)
    likes = models.ManyToManyField(User, related_name='likes_Article', blank=True)
    favories = models.ManyToManyField(User, related_name='favories_Article', blank=True)
    # pour image installe le : python -m pip install Pillow
     
    def __str__(self):
        return self.titre
    
    @property
    def non_categorie(self):
        return self.categorie.nom
    

    # juste pour recupere le nom de la categorie de la objet lie
    
class Commentaire(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_creation = models.DateField(auto_now_add=True)
    auteur = models.ForeignKey(User,on_delete=models.CASCADE)# (1,n)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)#sur un commentaire donne il peux avoir  ++ likes des user
    # mais user ne peux liker ++ fois se gere dans la vue 
    
    
    def __str__(self):
        return self.auteur.username

class like (models.Model):
    commentaire = models.ForeignKey(Commentaire, on_delete=models.CASCADE)
    auteur = models.ForeignKey(User,on_delete=models.CASCADE)# (1,n)
    
    
class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


'''
 ************** les relations entres les Classes ****************

'''

'''

Etudiant (n,n) Universite  ( ManyToMany) 

'''
 
class Etudiant (models.Model):
    matricule = models.CharField(max_length=7,unique=True) # ici le mat de etu est 7 caracteres pas plus pas moin d
    nom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    taille = models.FloatField(max_length=3) 
    tel = models.CharField(max_length=9, validators = [RegexValidator(r'^6\d{8}$','entrez un numero au format CMR')])
    
    def __str__(self):
        return self.nom
   

class Universite (models.Model):
    CHOIX_TYPE_UNI = [('Publique','Publique'), ('Para_Publique','Para_Publique'),('Privee','Privee')]
    nomUniver = models.CharField(max_length=200)
    typeUniver = models.CharField(max_length=255, choices=CHOIX_TYPE_UNI) # ici le chois de fera uniquement dans CHOIX_TYPE_UNI
    etu = models.ManyToManyField(Etudiant)
    
    def __str__(self):
        return self.nomUniver+' du type : '+self.typeUniver
    
    @property
    def non_etu(self):
        return self.etu.all()
    # juste pour recupere le nom de la categorie de la objet lie
    

'''
Personne (1,1) Adresse OnToOne 
'''
class Personne (models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    age = models.IntegerField()
    tel = models.CharField(max_length=9, validators = [RegexValidator(r'^6\d{8}$','entrez un numero au format CMR')])
    
    def __str__(self):
        return self.nom
    
class Adresse (models.Model):
    numroRue = models.IntegerField()
    ville = models.CharField(max_length=100)
    pesonne = models.OneToOneField(Personne,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.ville
    
    
    
'''
 **** gerer les dossier et employes ***
'''
class Reservation (models.Model):
    #'id', 'user', 'hotel', 'check_in', 'check_out'
    client = models.CharField(max_length=100)
    hotel = models.CharField(max_length=100)
    heureEntree = models.TimeField(null=False,blank=False)
    heureSortie = models.TimeField(null=False,blank=False)
   
   
   # mes models (relation (1,1) )
class Employe (models.Model):
    matricule = models.CharField(max_length=7,unique=True) # ici le mat de etu est 7 caracteres pas plus pas moin d
    nom = models.CharField(max_length=100)
    
class Dossier (models.Model):
    nom = models.CharField(max_length=100)
    contenue =  models.TextField()
    employe = models.OneToOneField(Employe,on_delete=models.CASCADE)
    
    
    

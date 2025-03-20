from datetime import date
from django.db import models
from django.core.validators import *
from django.contrib.auth.models import User, AbstractBaseUser



class Client(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    date_naissaince = models.DateField()
    tel = models.CharField(max_length=9, validators = [RegexValidator(r'^6\d{8}$','entrez un numero au format CMR')])
    email = models.EmailField(max_length=100)
    pays = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    quartier = models.CharField(max_length=100)
    photo_profil = models.ImageField(upload_to='images_articles',blank=True, null=True) 
    user = models.OneToOneField(User,on_delete=models.DO_NOTHING)
      

    def __str__(self):
        return self.nom
    
    
class Compte (models.Model):
    id_compte = models.BigAutoField(primary_key=True,validators=[MinValueValidator(10**9),MaxValueValidator(10**10-1)]) # genere 10 chiffres uniaue
    solde = models.IntegerField(null=False)
    date_creation = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(Client,on_delete=models.CASCADE) #(1,n)
    
    def __int__(self):
        return self.id_compte   
    
    
class Compte_Epargne (Compte): 
    id_compteE = models.BigAutoField(primary_key=True,validators=[MinValueValidator(10**9),MaxValueValidator(10**10-1)])
    taux_interet =  models.IntegerField()
    
    def __int__(self):
        return self.id_compteE
    
class Transaction (models.Model):
    type_trans = models.CharField(max_length=30)
    etat = models.BooleanField(choices=[(True,'SUCCES'),(False,'ECHEC')])
    date = models.DateTimeField(auto_now_add=True)
    montant  = models.IntegerField(null=False)
    ref = models.CharField(max_length=100)
    client = models.ForeignKey(Client,on_delete=models.CASCADE) #(1,n)
    
    def __str__(self):
        return self.ref
    

    

    



           



    

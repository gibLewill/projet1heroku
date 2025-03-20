from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

from wamybank.Form import *

# Create your views here.
def connexion_bank (req):
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
         message = 'Mot de Passe ou Login Incorecte'
         
    return render (req, 'connexion_bank.html', {'message':message})

def accueil (req):
    pass


def operations (req):
    op = ' suis les operarions'
    return render (req,'operations.html',{'op':op} )


def depot (req):
    op = ' ici les depots'
    return render (req,'depot.html',{'op':op} )


def retrait (req):
    op = ' ici les retraits'
    return render (req,'retrait.html',{'op':op})


def virement (req):
    op = ' ici les virements'
    return render (req,'virement.html',{'op':op})
   
            
def historique (req):
    op = ' ici les historiques'
    return render (req,'historique.html',{'op':op})

def listing (req):
    op = ' ici le listing des transactions '
    return render (req,'listing.html',{'op':op})

def gestion_compte (req):
    op = ' ici  gestion compte '
    return render (req,'gestion_compte.html',{'op':op})

def gestion_client (req):
    op = ' ici  gestion clients '
    return render (req,'gestion_client.html',{'op':op})
 
   
def creer_client (request):
   formulaire = Client_form()
   if request.method == 'POST':
       formulaire = Client_form(request.POST)
       if formulaire.is_valid():
          formulaire.save()
          message = 'creation Reussir'
          return render(request,'creer_client.html', {'message':message})
       else :
          formulaire = Client_form()
   return render(request,'creer_client.html', {'formulaire':formulaire})


def creer_compte (request):
   formulaire = CompteC_form()
   if request.method == 'POST':
       formulaire = CompteC_form(request.POST)
       if formulaire.is_valid():
          formulaire.save()
          message = 'creation Reussir'
          return render(request,'creer_compte.html', {'message':message})
       else :
          formulaire = CompteC_form()
   return render(request,'creer_compte.html', {'formulaire':formulaire}) 

def creer_compte_epargne (request):
   formulaire = CompteE_form()
   if request.method == 'POST':
       formulaire = CompteE_form(request.POST)
       if formulaire.is_valid():
          formulaire.save()
          message = 'creation Reussir'
          return render(request,'creer_compte_epargne.html', {'message':message})
       else :
          formulaire = CompteE_form()
   return render(request,'creer_compte_epargne.html', {'formulaire':formulaire})


def liste_client (request):
   clients  = Client.objects.all() # lobjet articles contient tous nos articles
   return render (request,'liste_client.html', {'lesClients': clients})
   
def liste_compteC (request):
   comptes  = Compte.objects.all() # lobjet articles contient tous nos articles
   return render (request,'liste_compteC.html', {'lesComptes': comptes})

def liste_compteE (request):
   comptes  = Compte_Epargne.objects.all() # lobjet articles contient tous nos articles
   return render (request,'liste_compteE.html', {'lesComptes': comptes})
   
   

 
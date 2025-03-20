from django import forms
from .models import Etudiant

'''    
# 1 ) je cree le formulaire pour mon model Etudiant deja importe dans .models
class Formulaire_Etu (forms.Form) :
    matricule = forms.CharField(label='Matricle :', max_length=7, required=True) # ici le mat de etu est 10 caracteres pas plus pas moin d
    nom = forms.CharField(label='Nom  :', max_length=100, required=True)
    date_naissance = forms.DateField(label=' Date de naissance :', required=True)
    taille = forms.FloatField(label='Taille :', max_length=3, required=True)
    
  
    class Meta: 
            model = Etudiant # mon moel puis ses champs ou attributs
            fiels = ('matricule' , 'nom','date_naissance','taille')
            
           
            

     # definition des label  en utlisant form de django
        matricule = forms.CharField(label='Matricle :', max_length=7) # ici le mat de etu est 10 caracteres pas plus pas moin d
        nom = forms.CharField(label='Nom  :', max_length=100)
        date_naissance = forms.DateField(label=' Date de naissance :')
        taille = forms.FloatField(label='Taille :', max_length=3)
    '''    

#2- Jutilise mon formulaire dans une vue

'''
Voici les étapes pour créer des données par l'utilisateur sur un formulaire en utilisant la classe qui hérite de CreateView dans Django :
Étape 1 : Créer un formulaire
Étape 2 : Créer une vue qui hérite de `CreateView`
    Créez ensuite une vue qui hérite de CreateView
Étape 3 : Configurer la vue dans l'URL 
Étape 4 : Créer un template pour la vue

Étape 1 : Créer un formulaire




Créez un fichier forms.py dans votre application Django et importez les modules nécessaires :

from django import forms
from .models import MonModele

Créez ensuite un formulaire pour votre modèle en héritant de la classe forms.ModelForm :

class MonFormulaire(forms.ModelForm):
    class Meta:
        model = MonModele
        fields = ('nom', 'prenom', 'email')  # champs à inclure dans le formulaire

Étape 2 : Créer une vue qui hérite de `CreateView`

Créez un fichier views.py dans votre application Django et importez les modules nécessaires :

from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import MonFormulaire
from .models import MonModele

Créez ensuite une vue qui hérite de CreateView :

class MonVue(CreateView):
    form_class = MonFormulaire
    model = MonModele
    template_name = 'mon_template.html'
    success_url = reverse_lazy('ma_vue')

Étape 3 : Configurer la vue dans l'URL

Créez un fichier urls.py dans votre application Django et importez les modules nécessaires :

from django.urls import path
from . import views

Créez ensuite une URL pour la vue :

urlpatterns = [
    path('mon_vue/', views.MonVue.as_view(), name='mon_vue'),
]

Étape 4 : Créer un template pour la vue

Créez un fichier mon_template.html dans votre dossier de templates et ajoutez-y le code suivant :

<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Envoyer</button>
</form>

Étape 5 : Tester la vue

Accédez à l'URL http://localhost:8000/mon_vue/ et remplissez le formulaire. Cliquez sur le bouton "Envoyer" pour créer une nouvelle instance de votre modèle.

Voilà ! Vous avez créé une vue qui permet à l'utilisateur de créer des données sur un formulaire en utilisant la classe qui hérite de CreateView.


'''
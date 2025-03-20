import re
from django import forms
from django.core.validators import *
from mesarticles.models import *

'''
# cette classe est ma classe de formulaire pour mon model Articles
1- etape 
'''
class ConnectionForm (forms.Form):
    nom = forms.CharField(max_length=100,label='Nom')
    matricule = forms.CharField(min_length=7, max_length=7, label='Votre Matricule') # ici le mat de etu est 7 caracteres pas plus pas moin d
   


class ArticleForm (forms.ModelForm):
    class Meta:
        model = Article
        fields = ['titre', 'contenu','categorie','image'] # Champs à éditer
        #1 ici et  en 2 point on cree sa vue dans view

class CommentaireForm (forms.ModelForm):
    class Meta:
        model = Commentaire
        fields = ['contenu']
    
        
class CategorieForm (forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['nom']
        
   
class UniversiteForm (forms.ModelForm):
    class Meta:
        model = Universite
        fields = ['nomUniver', 'typeUniver', 'etu']

class EtudiantForm (forms.ModelForm):
     class Meta:
        model = Etudiant
        fields = ['matricule', 'nom', 'date_naissance', 'taille', 'tel']
        widgets = {'date_naissance': forms.DateInput(attrs={'type': 'date'})}
        
        widgets = {
            'matricule': forms.TextInput(
                attrs={'placeholder': 'AB12345 (7 caractères max)'}
            ),
            'nom': forms.TextInput(
                attrs={'placeholder': 'Martin'}
            ),
            'date_naissance': forms.DateInput(
                attrs={'type': 'date', 'placeholder': 'YYYY-MM-DD'}
            ),
            'taille': forms.NumberInput(
                attrs={'placeholder': '1.75'}
            ),
            'tel': forms.TextInput(
                attrs={'placeholder': '623456789'}
            ),
        }
        
    # les methodes de validation automatique et informations direct a user
    # les Validations ( tres utilent pour le controle des donnees qui vont dans la bd 
    # reste ( sur le temple)
     def clean_nom(self):
        nom = self.cleaned_data['nom']
        if len(nom) < 3:
            raise forms.ValidationError(' le nom doit deppaser 3 caracteres')
        return nom
    
     def clean_taille(self):
          taille = self.cleaned_data['taille']
          if taille>200:
            raise forms.ValidationError('cette taille est invalide')
          return taille
      
     def clean_tel (self):
        tel = self.cleaned_data['tel']
        regex = r'^6\d{8}$'
        if not re.match(regex,tel):
            raise forms.ValidationError('entrez un numero au format CMR') 
        return tel
            
        
         
         
         
class PersonneForm (forms.ModelForm):
     class Meta:
        model = Personne
        fields = [ 'nom','prenom','date_naissance','age', 'tel']
        widgets = {'date_naissance': forms.DateInput(attrs={'type': 'date'})}
        
     def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['age'].widget.attrs['readonly']=True
        
        
     # permet de controler de facon auto les saisies    
     def clean(self):
        date_naissance = self.cleaned_data.get('date_naissance')
        if date_naissance:
             age = calcul_age(date_naissance)
             self.fields['age'].initail = age
        return self.cleaned_data 
    
    
def calcul_age (date_naissance):
    aujourdhui = date.today()
    age = aujourdhui.year - date_naissance.year - ((aujourdhui.month,aujourdhui.day) < (date_naissance.month,date_naissance.day))
    return age 



   
'''
     def clean_matricule(self):
        mat = self.cleaned_data.get('matricule')
        nom = self.cleaned_data.get('nom')
        if mat in nom:
            raise forms.ValidationError("Le mot de passe ne peut pas contenir votre nom.")
        return mat
'''
        

     
''''
 Exemlpe du cours formulaire dinscription

'''
class Form_Inscription (forms.Form):
    
        LES_PAYS = [('Cameroun','Cameroun'), ('Cote - Ivoire','Cote - Ivoire'), ('Benin','Benin'),('Togo','Togo')]
        CHOIX_TYPE_UNI = [('Publique','Publique'), ('Para_Publique','Para_Publique'),('Privee','Privee')]
        
        name = forms.CharField(max_length=50, required=True,label="Nom complet :")
        # utilsation des widget pour le format date
        dateNaissance = forms.DateField(widget=forms.DateInput , label="Date de Naissance :")
        sexe = forms.ChoiceField(choices=[('Masculin','Masculin'),('Feminin','Feminin')], widget=forms.RadioSelect)
        tel = forms.CharField( max_length=9, validators = [RegexValidator(regex=r'^[6][2-9]{8}$')])
        email = forms.EmailField(required=True, label="Adresse e-mail :")
        pays = forms.ChoiceField(choices=LES_PAYS)
        password = forms.CharField(widget=forms.PasswordInput, min_length=8, label="Mot de passe :")
        
        # mes methodes de controle avancees 
        # 1 mot de passe
        def clean_password(self): 
            password = self.cleaned_data.get('password')
            name = self.cleaned_data.get('name')
            
            if name in password:
                raise forms.ValidationError("Le mot de passe ne peut pas contenir votre nom.")
            return password

        # numero de tel

class ContactForm (forms.Form):
     nom = forms.CharField(max_length=50, required=True,label="Nom complet :")
     email = forms.EmailField(required=True, label="Adresse e-mail :")
     sujet = forms.CharField(max_length=60, required=True,label="sujet ici :")
     
     def clean_sujet(self):
         print(' def clean sujet')
         sujet = self.cleaned_data.get('sujet')
         print(sujet)
         if len(sujet)<5: 
           print('dans le if') 
           raise forms.ValidationError("le sujet doit contenir au moins 50 caracteres")
         return sujet
        
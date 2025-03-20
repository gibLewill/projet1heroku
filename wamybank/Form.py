

from django import forms
from .models import *


class Client_form (forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        
class CompteC_form (forms.ModelForm):
    class Meta:
        model = Compte
        fields = '__all__'
        
class CompteE_form (forms.ModelForm):
    class Meta:
        model = Compte_Epargne
        fields = '__all__'
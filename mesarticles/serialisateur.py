from rest_framework import serializers
from .models import Employe, Etudiant, Universite
 
'''
class MonModèleSerializer(serializers.ModelSerializer):
 class Meta:
 model = MonModèle
 fields = '__all__'
'''
 
class EtudiantSerialiser (serializers.ModelSerializer):
    class Meta:
        model = Etudiant
        fields = '__all__'
       
       
    # les Validations ( tres utilent pour le controle des donnees qui vont dans la bd)  
    # il se placent dans la classe du serialisateur pour les api  
    def validate_data (self,data):
         if data['matricule'] in data['nom']:
             raise serializers.ValidationError('le nom ne peut contenir le Matricule')
         return data
           
    def validate_nom(self,nom):
        if len(nom) < 3:
            raise serializers.ValidationError(' le nom doit deppaser 3 caracteres')
        return nom
    
    def validate_empty_values(self, data):
        return super().validate_empty_values(data)
    
    def validate_taille(self, taille):
        if taille>200:
            raise serializers.ValidationError(' cette taille est invalide')
        return taille
    
'''
Validation
 Un autre aspect important des sérializers est la validation des données. 
 Avant de sauvegarder des données dans la base, il 
 est crucial de s'assurer qu'elles sont valides et conformes aux attentes de l'application.
 DRF facilite cela en permettant de définir des règles de validation personnalisées au sein 
 des sérializers
'''  
# ensuite on par definir la vue du modelserial


# je voudrai egalement que mes universite soient afficher dans API

class UniversiteSerialiser (serializers.ModelSerializer):
    class Meta :
        model = Universite
        fields = ['nomUniver','typeUniver'] # ici je fais le choix des champs a afficher
        #fields = '__all__' # pour que tous les champs soient accessibles
        
class EmployeSerialiser (serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = '__all__'
        
    
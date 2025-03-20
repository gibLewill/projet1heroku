from django.contrib import admin
from .models import *
#cd C:\Users\ELITEBOOK 850 G3\Desktop\Formation Python\COURS COMPLETS PROF\DJANGO\projectDjango1

# Register your models here.
# ici on fait les migrations  bref on donne acces aux administrateurs

admin.site.register(Article)
admin.site.register(Commentaire)
admin.site.register(like)

admin.site.register(Categorie)
admin.site.register(Etudiant)
admin.site.register(Universite)
admin.site.register(Personne)
admin.site.register(Adresse)
admin.site.register(Employe)


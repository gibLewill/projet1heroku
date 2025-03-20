from django.contrib import admin

from .models import *

#cd C:\Users\ELITEBOOK 850 G3\Desktop\Formation Python\COURS COMPLETS PROF\DJANGO\projectDjango1

# Register your models here.
admin.site.register(Client)
admin.site.register(Compte)
admin.site.register(Compte_Epargne)
admin.site.register(Transaction)

from mesarticles.models import *

# pour rendre les variables visible globalement
def categories (request):
    categories = Categorie.objects.all()
    return {'categories':categories}
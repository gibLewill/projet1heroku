'''

Pour ajouter un type image à votre classe Article, vous devez utiliser le champ ImageField dans votre modèle. Voici un exemple :

# models.py
from django.db import models

class Article(models.Model):
    titre = models.CharField(max_length=255)
    contenu = models.TextField()
    image = models.ImageField(upload_to='images_articles', blank=True, null=True)

Dans cet exemple, nous avons ajouté un champ image de type ImageField à notre modèle Article. Le paramètre upload_to spécifie le répertoire où les images seront stockées.

Pour afficher l'image dans un template, vous pouvez utiliser la balise img et la propriété url du champ image :

<!-- template.html -->
<img src="{{ article.image.url }}" alt="{{ article.titre }}">

Assurez-vous d'avoir configuré correctement les paramètres de stockage des fichiers dans votre fichier settings.py :

# settings.py
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

Et assurez-vous d'avoir créé le répertoire media dans votre projet.

Pour uploader des images, vous pouvez utiliser un formulaire dans votre template :

<!-- template.html -->
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    <input type="file" name="image">
    <button type="submit">Uploader</button>
</form>

Et dans votre vue, vous pouvez traiter le fichier uploadé :

# views.py
from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def uploader_image(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('liste_articles')
    else:
        form = ArticleForm()
    return render(request, 'uploader_image.html', {'form': form})

Assurez-vous d'avoir créé un formulaire ArticleForm qui inclut le champ image :

# forms.py
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('titre', 'contenu', 'image')





'''


'''
Pour permettre seulement aux utilisateurs connectés de publier un article, vous pouvez utiliser la décoration @login_required de Django. Voici comment procéder :

1. Importez la décoration @login_required dans votre fichier views.py :

from django.contrib.auth.decorators import login_required

2. Ajoutez la décoration @login_required à la vue qui gère la création d'un article :

@login_required
def creer_article(request):
    # Code pour créer un article

Cela signifie que seule les utilisateurs connectés pourront accéder à cette vue et créer un article.

3. Si vous voulez également vérifier que l'utilisateur est connecté avant de sauvegarder l'article, vous pouvez utiliser la méthode is_authenticated dans votre vue :

def creer_article(request):
    if request.user.is_authenticated:
        # Code pour créer un article
    else:
        return redirect('login')

Cela redirigera les utilisateurs non connectés vers la page de connexion.

4. Enfin, vous pouvez également utiliser la classe LoginRequiredMixin pour créer une vue qui nécessite une connexion :

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView

class CreerArticleView(LoginRequiredMixin, CreateView):
    model = Article
    fields = ('titre', 'contenu', 'image')
    success_url = reverse_lazy('liste_articles')

Cela signifie que seule les utilisateurs connectés pourront accéder à cette vue et créer un article.

En suivant ces étapes, vous devriez être en mesure de limiter la création d'articles aux utilisateurs connectés.



###########################

La pagination est une fonctionnalité qui permet de diviser un grand nombre de données en plusieurs pages, ce qui améliore la navigation et la performance de votre site web.

Pour faire la pagination des templates HTML dans Django, vous pouvez suivre les étapes suivantes :

1. Installer le paquet `django.core.paginator` :

Vous n'avez pas besoin d'installer un paquet supplémentaire, car django.core.paginator est inclus dans Django.

2. Créer un paginateur :

Dans votre vue, créez un paginateur en utilisant la classe Paginator :

from django.core.paginator import Paginator

def ma_vue(request):
    # Récupérer les données à paginer
    donnees = MonModele.objects.all()

    # Créer un paginateur
    paginateur = Paginator(donnees, 10)  # 10 éléments par page

    # Récupérer la page actuelle
    page_actuelle = request.GET.get('page')

    # Récupérer les données pour la page actuelle
    donnees_page_actuelle = paginateur.get_page(page_actuelle)

    # Rendre le template avec les données paginées
    return render(request, 'mon_template.html', {'donnees': donnees_page_actuelle})

3. Ajouter la pagination dans le template :

Dans votre template, ajoutez les éléments suivants pour afficher la pagination :

<!-- mon_template.html -->

<!-- Afficher les données paginées -->
{% for donnee in donnees %}
    {{ donnee }}
{% endfor %}

<!-- Afficher les liens de pagination -->
{% if donnees.has_previous %}
    <a href="?page={{ donnees.previous_page_number }}">Précédent</a>
{% endif %}

{% for page in donnees.paginator.page_range %}
    {% if page == donnees.number %}
        <strong>{{ page }}</strong>
    {% else %}
        <a href="?page={{ page }}">{{ page }}</a>
    {% endif %}
{% endfor %}

{% if donnees.has_next %}
    <a href="?page={{ donnees.next_page_number }}">Suivant</a>
{% endif %}

En suivant ces étapes, vous devriez être en mesure de paginer vos données dans Django.

'''
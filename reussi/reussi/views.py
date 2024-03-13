from django.shortcuts import render


def accueil_rendu(request):
    import random
    nb = random.randint(0, 100)
    categorie=["homme","femme","enfants"]
    context = {"chiffre_aleatoire": nb, "liste" : categorie}
    page = render(request, "accueil.html", context)
    return page

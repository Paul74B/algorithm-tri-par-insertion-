from time import *
from random import randint

def genere_liste_aleatoire(n, maximum):
    """
    Cette fonction génère une liste aléatoire de n entiers compris entre 1 et maximum.

    pre:
        n (int): le nombre d'entiers à générer dans la liste.
        maximum (int): la valeur maximale de chaque entier.

    post:
        list: une liste de n entiers aléatoires compris entre 1 et maximum.
    """
    liste = []
    for i in range(n):
        liste.append(randint(1, maximum))
    return liste

def generer_meilleur_cas(n, maximum):
    """
    Cette fonction génère le meilleur cas pour le tri par insertion, c'est-à-dire une liste triée de n entiers compris entre 1 et maximum.

    pre:
        n (int): le nombre d'entiers à générer dans la liste.
        maximum (int): la valeur maximale de chaque entier.

    post:
        list: une liste triée de n entiers compris entre 1 et maximum.
    """
    liste = genere_liste_aleatoire(n, maximum)
    liste.sort()
    return liste

def generer_pire_cas(n, maximum):
    """
    Cette fonction génère le pire cas pour le tri par insertion, c'est-à-dire une liste triée en ordre décroissant de n entiers compris entre 1 et maximum.

    pre:
        n (int): le nombre d'entiers à générer dans la liste.
        maximum (int): la valeur maximale de chaque entier.

    post:
        list: une liste triée en ordre décroissant de n entiers compris entre 1 et maximum.
    """
    liste = genere_liste_aleatoire(n, maximum)
    liste.sort(reverse=True)
    return liste


t1 = time()
liste = generer_meilleur_cas(10000, 100)
print(liste)

def tri_insertion(liste_a_trier):
    """
    Cette fonction implémente l'algorithme de tri par insertion pour trier une liste donnée dans l'odre croissant.
    pre:
        liste_a_trier (list): la liste à trier.
    post:
        liste_a_trier: la liste triée.
    """
    # Parcourir la liste de la deuxième à la dernière valeur
    for i in range(1, len(liste_a_trier)):
        # Stocker la valeur à trier dans une variable temporaire (nombre)
        nombre = liste_a_trier[i]
        test = i - 1
         # Parcourir les éléments précédents (nombre) dans la liste
        while test >= 0 and nombre < liste_a_trier[test]:
            # Si la valeur est plus petite que la valeur précédente, décaler la valeur précédente vers la droite
            liste_a_trier[test + 1] = liste_a_trier[test]
            # Continuer à parcourir les éléments précédents
            test -= 1
        # modifie la valeur à la bonne position dans la liste triée
        liste_a_trier[test + 1] = nombre
    # Retourner la liste triée
        temps_encour = time()
        print("temps de traitement = ", temps_encour-t1)
    return liste_a_trier

print(tri_insertion(liste))

t2 = time()

temps = t2 - t1
print("Temps final d'execution = ", temps, "secondes")
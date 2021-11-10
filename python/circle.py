from math import pi

def circleArea(r):
    if type(r) not in [int, float] :
        raise TypeError("Le rayib doit être un nombre réel non négatif")
    if r < 0 :
        raise ValueError("Le rayon ne peut pas être négatif")
    return pi * (r**2)

# test
'''values = [4, -2, "coucou", 0] '''# série de valeurs que nous allons tester dans notre fonction.

# les tests sont fait à même le fichier, il n'y a pas de séparation entre les deux.
'''for v in values :
    res = circleArea(v)
    print(f"L'aire d'un cercle de rayon {v} est de : {res}")'''
# C'est assez fragile comme focntion car il n'est pas censé calculé un rayon négatif et ne pas essayer de calculer la chaîne de caractère. Elle a posé problème en entrée.
# Il faudrait prévoir une fonction plus stable qui prend en compte si ce n'est pas un int.
# C'est une approche qui fonctionne mais je n'ai pas réalisé au plein sans du terme un test unitaire avec des méthodes assertives.
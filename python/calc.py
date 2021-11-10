# Une focntion qui renvoie le ddouble de la valeur fournit en entrée
def double(x):
    return x * 2

def triple(x):
    return x * 3

# Ces deux fonctions en elle même ne vont pas me servir à même ce fichier. Elles vont servir de module importable pour un autre fichier.
# C'est un fichier d'appuie pour d'autres.
# Ces fonctions sont des fonctions pures car il n'y a pas de dépendance. Elle ne compte sur rien d'autre que le paramètre fournit en entrée.

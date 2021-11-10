import unittest
from circle import circleArea
from math import pi

class TestCircleModule(unittest.TestCase):
    def test_circleArea(self):
        self.assertAlmostEqual(circleArea(1),pi) # il va checker les 6 ou 7 première décimals et regarder dans celle la. Mais c'est déjà pas mal.
    def test_circleArea(self):
        self.assertAlmostEqual(circleArea(0), 0) 
    def test_circleArea(self):
        self.assertAlmostEqual(circleArea(2.1), pi*(2.1**2)) 

# python3 -m unittest  test_circle.py
# 1 test ok ! car une méthode = 1 test même si plusieurs tests dans la méthode

# python3 -m unittest : en lancant cette commande, il cumule touts les fichiers tests présent dans le dossier.
# Un fail suffit pour faire échec le retour du test mais si ce n'est que 1/3

# assertRaises : permet de tester une exception, par eexemple si on nous donnes des valeurs qui ne sont pas sensé être données.
    #def test_values(self):
        self.assertRaises(ValueError, circleArea, -2) # assert.raises n'a pas renvyé de true et nous a permis de savoir que l'exception levée et de type ValueError
        # après avoir trouver l'erreur et son type, nous avons pu ajouter une nouvelle gestion d'erreur à notre fonction.
    
    def test_types(self) :
        # self.assertRaises(TypeError, circleArea, "coucou")
        self.assertRaises(TypeError, circleArea, 1)

# en faisant echo $? : si mon unittest renvoie un fail pour 1 test sur 4, la commande renvoie quand même 1 car il y a eu une erreur.

# python3 -m unittest && echo $? : si la première partie de la commande est en échec alors seconde partie (echo $?) ne sera pas exécuté !
# Il faut utiliser le || 
# python3 -m unittest && echo $? : la les deux parties sont exécutées
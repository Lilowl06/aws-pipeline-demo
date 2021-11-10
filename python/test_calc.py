# C'est une convention de nommage qui sera utilisé par le module unittest.
import unittest
from calc import double, triple 
# un fichier va travailler sur l'autre

# pour obéir au règle d'écriture imposé par le module unittest, il faut écrire une classe.
#class TestDouble(unittest.TestCase): # classe implémenté pour effectuer des tests. Il en existe plusieurs mais c'est celui qui nous convient. La classe testDouble héritera de toutes les fonctionnalités de TestCase.
#    def test_double(self):
#        self.assertEqual(double(6), 12) #comme self hérite de toutes les autres montrent de la classe parente TestCase. Donc self peut référencer ou faire appel à des membres de la classe TestCase.
        # Donc la méthode assertEqual permet de faire un déclaration (assert = délcaration) et assertEqual : permet de faire une comparaison. 
        # L'invocation de double à qui je passerai 6 en entrée (en premier argument) doit être égale à 12 que je donne en second argument

# Ici c'est une classe que l'on a rédigé mais dont on ne se sert pas, car il y a aucune utilisation, interprétation.
# Pour l'utiliser il faut faire dans l'interpréteur de commande : python3 -m unittest test_calc.py
# Il n'y a pas d'interprétation direct mais on délègue à testUnitaire le choix de faire ca sauce.

# Maintenant nous testons toutes les fonctions de notre module calc :
class TestCalc(unittest.TestCase):
    def test_double(self):
        self.assertEqual(double(6), 12)

    def test_triple(self):
        self.assertEqual(triple(6), 18)
        # self.assertEqual(triple(6), 19)
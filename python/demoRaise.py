# Est ce que le try excet laisse une erreur ?
def demo(n):
    if n > 10 :
        raise ValueError("n ne peut pas être supérieur à 10")
    # La fonction return none ici.

demo(5)
demo(11)
# print("The end ...") # le print ne s'affichera jamais car le programme crash avant sur le demo(11), le raise permet de lever l'erreur mais n'évite pas le crash du programme

# si on veut réagir, on se sert du try except et on va chercher à capter l'erreur car sinon le programme va cracher.
'''try :
    demo(11)
except ValueError :
    print("Mauvaise valeur founie en entrée...")
except :
    print("Le programme a rencontré une erreur,")'''

print("The end ...") # nous ne sommes pas sortie sortie du programme est nous avons atteint le print.

# echo $? : Elle contient toujours le code retour du processus qui vient de s'arrêter ! 0 pas d'erreur tout c'est bien passé et 1 le processus s'est arrêté de manière anormal.
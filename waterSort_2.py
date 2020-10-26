"""
Created on Sun Oct 25 22:18:24 2020

@author: PI314
"""

#algo pratiquemment pret mais il faut revoir la fonction remplir ou remplissable 
# cest une hypothese parce qu il y a des doublons

#il faut executer l autre fichier en premier et bien penser à les placer dans le meme repertoire

import waterSortFunctions
from random import *

rose = "rose"
orange="orange"
gris="gris"
bleuf="bleuf"
vert="vert"
bleuc="bleuc"
rouge="rouge"
gris="gris"
kaki="kaki"
violet="violet"

tube1 =[orange, violet, gris, violet]
tube2 =[violet, bleuc, bleuc, vert]
tube3 =[vert, vert, gris, rouge]
tube4 =[bleuf, gris, bleuf, rouge]
tube5 =[orange, violet, rose, rose]
tube6 =[bleuc, kaki, bleuf, bleuf]
tube7 =[bleuc, rouge, rose, orange]
tube8 =[gris, vert, rouge, orange]
tube9 =[kaki, kaki, kaki, rose]
tube10=[]
tube11=[]

tube1bis =(orange, violet, gris, violet)
tube2bis =(violet, bleuc, bleuc, vert)
tube3bis =(vert, vert, gris, rouge)
tube4bis =(bleuf, gris, bleuf, rouge)
tube5bis =(orange, violet, rose, rose)
tube6bis =(bleuc, kaki, bleuf, bleuf)
tube7bis =(bleuc, rouge, rose, orange)
tube8bis =(gris, vert, rouge, orange)
tube9bis =(kaki, kaki, kaki, rose)
tube10bis=()
tube11bis=()



liste_tube = [tube1, tube2, tube3, tube4, tube5, tube6, tube7, tube8, tube9]
liste_etat = []
liste_aux = ()
liste_actions = []

while not(termine(liste_tube)):
    print("NOUVEL ESSAI")
    liste_tube = [list(tube1bis), list(tube2bis), list(tube3bis), list(tube4bis), list(tube5bis), list(tube6bis), list(tube7bis), list(tube8bis), list(tube9bis), list(tube10bis), list(tube11bis)]
    liste_etat = []
    liste_aux = ()
    liste_actions = []
    action = chercher_remplissable(liste_tube)
    a = randint(0, len(action)//2-1)
    action1 = action[2*a]
    action2 = action[2*a + 1]
    action = [[action1, action2]]
    liste_actions += action
    remplir(liste_tube[action1], liste_tube[action2])
    liste_aux = [0] * len(liste_tube)
    for k in range(len(liste_tube)):
        liste_aux[k] = tuple(liste_tube[k])
    
    liste_etat += [liste_aux]
            
            
    for i in range(40):
        print(i , "de la boucle for")
        if not(termine(liste_tube)):
            action = chercher_remplissable(liste_tube)
            if action == []:
                break
            a = randint(0, len(action)//2-1)
            action1 = action[2*a]
            action2 = action[2*a + 1]
            action = [[action1, action2]]
            liste_actions += action
            remplir(liste_tube[action1], liste_tube[action2])
            liste_aux = [0] * len(liste_tube)
            for k in range(len(liste_tube)):
                liste_aux[k] = tuple(liste_tube[k])
            
            liste_etat += [liste_aux]
            for j in range(len(liste_tube)):
                print(j ,liste_tube[j])
            
print(liste_actions)
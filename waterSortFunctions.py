
"""
Created on Thu Oct 22 19:08:35 2020

@author: PI314
"""

def remplissable(tube1, tube2):
    couleur1 = 0
    couleur2 = 0
    if len(tube1) > 0:
        couleur1 = tube1[-1]
    if len(tube2) > 0:
        couleur2 = tube2[-1]
            
    return (len(tube1) < 4 and couleur1 == couleur2 and couleur1 != 0 and couleur2 != 0) or (len(tube1) == 0 and len(tube2)>0)
    
def remplir(tubeARemplir, tubeAVider):
    bloc1 = bloc(tubeARemplir)
    
    for i in range(2):
        if len(tubeAVider) > 0:
            if remplissable(tubeARemplir, tubeAVider):
                tubeARemplir += [str(tubeAVider.pop())]



#def remplir(tubeARemplir, tubeAVider):
#    bloc1 = bloc(tubeAVider)
#    if remplissable(tubeARemplir, tubeAVider):
#        for i in range(1, 4-len(tubeARemplir)):
#            if i < bloc1:
#                tubeARemplir += [str(tubeAVider.pop())]
        
def chercher_remplissable(liste_tube):
    liste = []
    for i in range(len(liste_tube)):
        if bloc(liste_tube[i]) < 4:
            for j in range(len(liste_tube)):
                if bloc(liste_tube[j]) < 4:
                    if j != i:
                        if remplissable(liste_tube[i], liste_tube[j]):
                            liste += [i, j]
    
    return liste

#def retourner_liste(liste):
#    liste1 = liste
#    return liste1
    

def bloc(tube):
    l = 0
    if len(tube) > 0:
        l = 1
    if len(tube) > 1 and tube[-1] == tube[-2]:
        l = 2
    if len(tube) > 2 and tube[-1] == tube[-2] and tube[-2] == tube[-3]:
        l = 3
    if len(tube) > 3 and tube[-1] == tube[-2] and tube[-2] == tube[-3] and tube[-3] == tube[0]:
        l = 4
    return l

def termine(liste_tube):
    etat = True
    for i in range(len(liste_tube)):
        if bloc(liste_tube[i])!=4 and bloc(liste_tube[i])!=0:
            etat = False
    return etat
            
        
    
def reecrire_etape(liste_etape): #en gros rajoute plus 1
    for i in range(len(liste_etape)):
        liste_etape[i][0] += 1
        liste_etape[i][1] += 1
        
    
    

        
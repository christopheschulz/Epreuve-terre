# Inverser une chaîne

import sys

arguments = sys.argv

def inverser(chaine):
    resultat = []
   
    for i in range(len(chaine)-1,-1,-1):
        resultat.append(chaine[i])
    
    return "".join(resultat)

if len(arguments) == 2:
    print(inverser(arguments[1]))
   
else:
    print("Mmm ... Il y a comme un problème !")
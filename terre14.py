# Trié ou pas

import sys
import copy

args = sys.argv[1:]

def est_triee(liste):
    liste_a_verifier = copy.copy(liste)
    liste_trie =[]
    
    while liste_a_verifier:
            liste_trie.append(min(liste_a_verifier))
            liste_a_verifier.remove(min(liste_a_verifier))

    return liste_trie == liste
    


if  all(arg.isdigit() for arg in args):
    args_int = [int(arg) for arg in args]
    
    if est_triee(args_int):
         print("Triée")
    else:
         print("Pas trié")
    
else:
    print("erreur.")
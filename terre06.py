# Inverser une chaîne

import sys

args = sys.argv[1:]

def inverser(chaine):
    resultat = []
   
    for i in range(len(chaine)-1,-1,-1):
        resultat.append(chaine[i])
    
    return "".join(resultat)

def main():
    if len(args) == 1:
        print(inverser(args[0]))
    else:
        print("Mmm ... Il y a comme un problème !")

if __name__ == "__main__":
    main()
# Inverser une chaîne

import sys

arguments = sys.argv[1:]

def inverser(chaine):
    resultat = []
   
    for i in range(len(chaine)-1,-1,-1):
        resultat.append(chaine[i])
    
    return "".join(resultat)

def main():
    if len(arguments) == 1:
        print(inverser(arguments[0]))
    else:
        print("Mmm ... Il y a comme un problème !")

if __name__ == "__main__":
    main()
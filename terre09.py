# Racine carrée d’un nombre

import sys

args = sys.argv[1:]

def racine_carre(a):
    result = int(a)**0.5
    if result.is_integer():
        return int(result)
    else:
        return round(result,2)
  
if len(args) == 1 and args[0].isdigit():
    print(racine_carre(args[0]))
else:
    print("Mmm ... Quelquechose cloche !")
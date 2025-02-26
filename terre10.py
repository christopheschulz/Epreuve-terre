# Nombre premier

import sys

args = sys.argv[1:]

def nombre_premier(a):
    a = int(a)
    if a == 0 or a == 1:
        return False
    
    for i in range(1,a):
        if a%i == 0:
            return False
        
    return True
    
  
if len(args) == 1 and args[0].isdigit():
    if nombre_premier(args[0]):
        print(f"Oui, {args[0]} est un nombre premier")
    else:
        print(f"Non, {args[0]} n'est pas un nombre premier")
else:
    print("Mmm ... Quelquechose cloche !")
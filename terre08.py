# Puissance d’un nombre

import sys

args = sys.argv

def puissance(a,b):
    result = 1
  
    for i in range(int(b)):
        result *= int(a)
    return result

if len(args) == 3 and args[1].isdigit() and args[2].isdigit():
    print(puissance(args[1],args[2]))
else:
    print("Mmm ... Quelquechose cloche !")
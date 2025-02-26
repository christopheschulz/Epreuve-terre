# Puissance d’un nombre

import sys

args = sys.argv[1:]

def puissance(a,b):
    result = 1
  
    for i in range(int(b)):
        result *= int(a)
    return result

if len(args) == 2 and all(arg.isdigit() for arg in args):
    print(puissance(args[0],args[1]))
else:
    print("Mmm ... Quelquechose cloche !")
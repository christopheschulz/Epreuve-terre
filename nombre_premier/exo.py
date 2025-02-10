import sys

args = sys.argv

def nombre_premier(a):
    a = int(a)
    if a == 0 or a == 1:
        return False
    
    for i in range(1,a):
        if a%i == 1:
            return False
    return True
    
  
if len(args) == 2 and args[1].isdigit():
    if nombre_premier(args[1]):
        print(f"Oui, {args[1]} est un nombre premier")
    else:
        print(f"Non, {args[1]} n'est pas un nombre premier")
else:
    print("Mmm ... Quelquechose cloche !")
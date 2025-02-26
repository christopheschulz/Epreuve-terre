import sys

args = sys.argv

def racine_carre(a):
    result = int(a)**0.5
    if result.is_integer():
        return int(result)
    else:
        return round(result,2)
  
if len(args) == 2 and args[1].isdigit():
    print(racine_carre(args[1]))
else:
    print("Mmm ... Quelquechose cloche !")
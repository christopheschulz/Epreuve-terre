import sys

args = sys.argv

def trouver_la_suisse(*args):
    resultat = 0
    int_arg =[int(arg) for arg in args[0]]

    for arg in int_arg:
        if arg != min(int_arg) and arg != max(int_arg):
            resultat = arg
      
    if not resultat:
        return "erreur."
    
    return resultat



if len(args) == 4 and all(arg.isdigit() for arg in args[1:]):
    print(trouver_la_suisse(args[1:]))
else:
    print("il semblerai bien que vous n'ayez pas 3 arguments ou qu'ils ne soient pas des entiers !")
# Taille d’une chaîne

import sys

args = sys.argv[1:]

if len(args) == 1 and not args[0].isdigit():
    print(len(args[0]))
else:
    print("erreur.")
    
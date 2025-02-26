# Divisions

import sys

arguments = sys.argv
print(arguments)

try:
    if len(arguments) == 3 and int(arguments[2]) != 0 and int(arguments[1]) // int(arguments[2]) != 0:
            print(f"résultat : {int(arguments[1]) // int(arguments[2])}")
            print(f"reste: {int(arguments[1]) % int(arguments[2])}")
            exit()
except ValueError:
      print("erreur.")
     

        


import sys
arguments = sys.argv

if len(arguments) == 2 and not arguments[1].isdigit():
    print(len(arguments[1]))
else:
    print("erreur.")
    
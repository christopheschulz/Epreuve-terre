import string
import sys

argument = sys.argv
alphabet = string.ascii_lowercase

if len(argument) > 2 or len(argument) == 1:
    print("Veuillez vérifier le nombre d'argument passé! Il (ne) doit y en avoir (qu')un !")
    sys.exit()
if argument[1].lower() not in alphabet:
    print("L'argument doit être une lettre de l'alphabet!")
    sys.exit()

indice_argument = alphabet.index(argument[1])

for i in range(indice_argument, len(alphabet)):
    print(alphabet[i],end="")
print()

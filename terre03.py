# L’alphabet à partir de

import sys

args = sys.argv[1:]

alphabet = ""
for i in range(97,123):
    alphabet+= chr(i)

def args_are_valid():
    if len(args) > 1:
        print("Veuillez vérifier le nombre d'argument passé! Il (ne) doit y en avoir (qu')un !")
        return False
    elif args[0].lower() not in alphabet:
        print("L'argument doit être une lettre de l'alphabet!")
        return False
    return True


def main():
    if args_are_valid():
        indice_argument = alphabet.index(args[0])

        for i in range(indice_argument, len(alphabet)):
            print(alphabet[i],end="")
        print()


if __name__ == "__main__" :
    main()
# Divisions

import sys

args = sys.argv[1:]


def args_are_valid():
     if len(args) != 2:
          return False
     return True
     
def main(): 
    if args_are_valid():
        try:
            a = int(args[0])
            b =int(args[1])
            if b != 0 and a // b != 0:
                print(f"résultat : {a // b}")
                print(f"reste: {a % b}")
        except ValueError as e:
            print("e")
    else:
         print("erreur.")
if __name__ == "__main__":
      main()
     

        


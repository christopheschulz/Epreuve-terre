# Pair ou impair

import sys

args = sys.argv[1:]

def args_are_valid():
    if len(args) > 1  :
        print("Tu ne me la mettras pas à l'envers")
        return False
    return True

def main():
    if args_are_valid():
        try:
            int_arg = int(args[0])
            if abs(int_arg) % 2 == 0:
                print("pair")
            else:
                print("impair")
        except ValueError:
            print("Tu ne me la mettras pas à l'envers")
            sys.exit()


if __name__ == "__main__":
    main()
import sys

argument = sys.argv

if len(argument) >2 or len(argument) == 1  :
    print("Tu ne me la mettras pas à l'envers")
    exit()
try:
    int_arg = int(argument[1])
except ValueError:
    print("Tu ne me la mettras pas à l'envers")
    exit()

if abs(int(argument[1])) % 2 == 0:
    print("pair")
else:
    print("impair")
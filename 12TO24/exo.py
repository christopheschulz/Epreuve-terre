import sys

args = sys.argv

def transfrom_12_to_24(chaine):
    split_chaine = chaine.split(":")
    if len(split_chaine[0])==2 and split_chaine[0].isdigit() and split_chaine[1][:2].isdigit() and len(split_chaine[1]) == 4 :
        heures = int(split_chaine[0]) 
        minutes = int(split_chaine[1][:2])
        PM_heure = split_chaine[1][-2:]

        if PM_heure.lower() == "pm":
            heures = heures + 12
        
        return f"{heures}:{minutes}"
       
    return "Mmm ... il y a anguille sous roche"



if len(args) == 2 and ":" in args[1]:
    print(transfrom_12_to_24(args[1]))
else:
    print("Mmm ... il y a anguille sous roche")





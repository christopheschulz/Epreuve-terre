import sys

args = sys.argv

def transfrom_24_to_12(chaine):
    split_chaine = chaine.split(":")
    PM_heure = "Am"
    if len(split_chaine)==2 and split_chaine[0].isdigit() and split_chaine[1].isdigit():
        heures = int(split_chaine[0]) 
        minutes = int(split_chaine[1])

        if 12 < heures < 24:
            PM_heure="PM"
            heures = heures - 12
        if heures == 12:
            PM_heure="PM"
    
        return f"{heures}:{minutes} {PM_heure}"

    return "Mmm ... il y a anguille sous roche"



if len(args) == 2 and ":" in args[1]:
    print(transfrom_24_to_12(args[1]))
else:
    print("Mmm ... il y a anguille sous roche")
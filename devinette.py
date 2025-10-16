import random

chiffre_a_trouver = 23

nbr_user = int(input("Trouvez le chiffre à deviner : "))

while nbr_user != chiffre_a_trouver :
    nbr_user = int(input("Trouvez le chiffre à deviner : "))


    if nbr_user == chiffre_a_trouver :
        print("Gagné !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

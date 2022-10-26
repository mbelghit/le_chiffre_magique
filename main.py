def demander_nombre (nb_min, nb_max):
    nb_int = 0 
    while nb_int == 0 :
        nb_str = input(f"quel est le nombre magique (entre {nb_min}  et {nb_max}) ?")
        try : 
            nb_int = int(nb_str)
        except ValueError:
            print("ERREUR : vous devez ecrire un nombre")
        else : 
            if nb_int<nb_min or nb_int > nb_max :
                print(f"ERRREUR : vous devez entree un nombre entre {nb_min} et {nb_max}")
                nb_int = 0
   
    return nb_int






NOMBRE_MIN = 1
NOMBRE_MAX = 10
NOMBRE_MAGIQUE = 5
NB_VIES = 4



nombre = 0
vies = NB_VIES
while not nombre == NOMBRE_MAGIQUE and vies > 0:
    print(f"il vous reste {vies} vies")
    nombre = demander_nombre(NOMBRE_MIN, NOMBRE_MAX)
    if nombre > NOMBRE_MAGIQUE :
        print("le nombre magique est plus petit !")
        vies -= 1
    elif nombre < NOMBRE_MAGIQUE :
        print("le nombre magique est plus grand !")
        vies -= 1
    elif nombre == NOMBRE_MAGIQUE :
        print("bravo vous avez gagne")

if vies == 0 :
    print("vous avez perdu!")
nb=int(input("entrez un nombre entre 10 et 20: "))
if nb>=10 and nb<=20:
        print("nombre valide")
else:
        while True:
            nb = int(input("entrez un nombre entre 10 et 20: "))
            if nb>=10 and nb<=20:
                print("nombre valide")
                break
            elif nb<10:
                print("nombre trop petit")
            else:
                print("nombre trop grand")

    
def entier():
    while True:
        nbstr = input("Entrez un chiffre entier : ")

        try:
        
            nombre = float(nbstr)
            
        
            if nombre == int(nombre):
            
                nb = int(nombre)
                break
            else:
            
                print("Ceci n'est pas un nombre entier. Veuillez réessayer.")
        
                
        except ValueError:
        
            print("Entrée invalide (ce n'est pas un nombre). Veuillez réessayer.")
        

    print(f"Vous avez entré l'entier valide : {nb}")

entier()

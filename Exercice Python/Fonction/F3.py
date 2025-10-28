def nombredevoyelles():
 mot = str(input("Entrez un mot ou une phrase : "))
 VOYELLES = "aeiouyAEIOUY"
 nombre_voyelles = len([caractere for caractere in mot if caractere in VOYELLES])
 print(f"Le texte entré est : '{mot}'")
 print(f"Le nombre de voyelles est : {nombre_voyelles}")

nombredevoyelles()

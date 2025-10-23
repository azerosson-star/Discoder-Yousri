# Programme d'affectation d'un tarif d'assurance selon :
# - ancienneté du permis (années)
# - âge du conducteur (années)
# - nombre d'accidents dont il est responsable

# Lecture des données utilisateur (entiers)
anciennete = int(input("Depuis combien d'années avez-vous votre permis ? "))
age = int(input("Quel est votre âge ? "))
accidents = int(input("De combien d'accidents étiez-vous responsable ? "))

# Validation simple : interdire les valeurs négatives
if anciennete < 0 or age < 0 or accidents < 0:
    print("Entrée invalide : les valeurs ne peuvent pas être négatives.")
else:
    # Règles de décision (ordre important) :
    # 1) Si la personne a des accidents ET est jeune ou peu expérimentée => refus
    # 2) Sinon si aucun accident et ancienneté >=2 et age >=25 => meilleur tarif (vert)
    # 3) Sinon si aucun accident et (ancienneté >=2 ou age >=25) => tarif moyen (orange)
    # 4) Sinon => tarif élevé (rouge)

    if accidents > 0 and (anciennete < 2 or age < 25):
        print("La compagnie refuse de vous assurer")
    elif accidents == 0 and anciennete >= 2 and age >= 25:
        print("Vous vous voyez attribuer le tarif vert")
    elif accidents == 0 and (anciennete >= 2 or age >= 25):
        print("Vous vous voyez attribuer le tarif orange")
    else:
        print("Vous vous voyez attribuer le tarif rouge")


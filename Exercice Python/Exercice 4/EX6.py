print("Entrez le scores des quatres candidats sans % :")
candidat1=float(input("candidat 1 : "))
candidat2=float(input("candidat 2 : "))
candidat3=float(input("candidat 3 : "))
candidat4=float(input("candidat 4 : "))
if candidat1>=50:
    print("Un candidat 1 a obtenu la majorité absolue et est élu au premier tour.")
elif candidat2>=50:
    print("Un candidat 2 a obtenu la majorité absolue et est élu au premier tour.")
elif candidat3>=50:
    print("Un candidat 3 a obtenu la majorité absolue et est élu au premier tour.")
elif candidat4>=50:
    print("Un candidat 4 a obtenu la majorité absolue et est élu au premier tour.")
else:
    print("Aucun candidat n'a obtenu la majorité absolue. Un second tour est nécessaire.")

if (candidat1>candidat2) and (candidat1>candidat3) and (candidat1>candidat4):
    print("le candidat 1 se trouve en ballotage favorable. ")
else:
    print("le candidat 1 ne se trouve pas en ballotage defavorable. ")


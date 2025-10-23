from math import factorial


n=int(input("nb chevaux partants : "))
a=int(input("nb chevaux joués : "))
print(f"Dans l'ordre :",{factorial(n)//factorial(n-a)})
print(f"Hors ordre :",{factorial(n)//(factorial(a)*factorial(n-a))})
# le signe // permet d'effectuer une division entière c'est à dire que le resultat sera toujours un entier
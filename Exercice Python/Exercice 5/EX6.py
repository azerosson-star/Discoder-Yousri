n=int(input("Entrez un nombre : " ))
prod = 1
s = "1"
for i in range(2, n + 1):
        s = s + " x " + str(i)
        prod *= i
print(f"{s}")

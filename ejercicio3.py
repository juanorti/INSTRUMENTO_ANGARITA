numeros=[1,2,3,4,5,6,7,8,9,10]
print("Imprimendo con ciclo for")
for i in range(len(numeros)):
    print(numeros[i], end=" " )

print("\nImprimendo con ciclo while")
i=0
while i < len(numeros):
    print(numeros[i], end=" ")
    i+=1
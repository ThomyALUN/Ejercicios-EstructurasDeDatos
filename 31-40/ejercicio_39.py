# 39. Para un vector (lista) de números enteros.
# Calcular e imprimir la suma de los valores pares y el promedio de los impares.

from funciones import generarVector

vector=generarVector(6,0,15)
print(vector)

sumaPares=0
sumaImpares=0
cantImpares=0

for i in range(len(vector)):
    if vector[i]%2==0:
        sumaPares+=vector[i]
    else:
        sumaImpares+=vector[i]
        cantImpares+=1

promImpares=sumaImpares/cantImpares
print(f"La suma de los valores pares es: {sumaPares}")
print(f"El promedio de los valores impares es: {promImpares}")
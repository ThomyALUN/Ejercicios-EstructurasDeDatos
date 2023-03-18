# 37. Leer un vector (lista) y un valor. 
# Determinar e imprimir si el valor se encuentra en el vector y cuántas veces.

from funciones import generarVector

veces=0
size=10
vector=generarVector(size, limInf=0, limSup=10)
print(vector)

valor=int(input("Ingrese un valor a buscar: "))
for i in range(size):
    if vector[i]==valor:
        veces+=1

print(f"El valor {valor} se encontró {veces} veces")
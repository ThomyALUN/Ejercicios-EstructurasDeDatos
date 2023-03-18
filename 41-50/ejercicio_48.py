# 48. Leer 2 vectores, calcular y escribir si son iguales.

from funciones import generarVector

size=5

vector1=generarVector(size,0,10)
print(vector1)

vector2=generarVector(size,0,10)
print(vector2)

iguales=True
for i in range(size):
    if vector1[i]!=vector2[i]:
        iguales=False
        break

print(f"¿Los vectores son iguales?: {iguales}")
print(vector1==vector2)

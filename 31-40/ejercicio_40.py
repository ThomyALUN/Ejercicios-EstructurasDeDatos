# 40. Leer un vector (lista) de enteros, escribir los valores múltiplos de 7.

from funciones import generarVector

vector=generarVector(20,0,100)
print(vector)

for i in range(len(vector)):
    if vector[i]%7==0:
        print(f"El valor en la posición {i+1} es múltiplo de 7: {vector[i]}")
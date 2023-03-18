# 41. Para un vector (lista), calcular y escribir el número de valores repetidos del vector.

from funciones import generarVector

vector=generarVector(10,0,10)
print(vector)
listaRepetidos=[]

for i in range(len(vector)-1):
    for j in range(i+1,len(vector)):
        if vector[i]==vector[j] and vector[i] not in listaRepetidos:
            listaRepetidos.append(vector[i])

print(listaRepetidos)
print(f"Hay {len(listaRepetidos)} elementos repetidos una o más veces")
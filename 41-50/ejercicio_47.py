# 47. Dado un vector, generar otros dos vectores; 
# uno, con los elementos pares y otro, 
# con los elementos pares del vector original.

from funciones import generarVector

vector=generarVector(10,0,10)
print(vector)

pares=[]
impares=[]

for i in range(len(vector)):
    valor=vector[i]
    if valor%2==0:
        pares.append(valor)
    else:
        impares.append(valor)

print(pares)
print(impares)
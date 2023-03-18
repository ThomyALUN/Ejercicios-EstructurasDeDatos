# 42. Leer un vector, generar otro que devuelva los mismos elementos pero sin elementos repetidos.

from funciones import generarVector

vector=generarVector(10,0,10)
print(vector)

vectorNoRept=[]
for i in range(len(vector)):
    if vector[i] not in vectorNoRept:
        vectorNoRept.append(vector[i])

print(vectorNoRept)
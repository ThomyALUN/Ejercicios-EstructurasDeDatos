# 43. Leer un vector, calcular y escribir su norma.

from funciones import generarVector

vector=generarVector(5,0,10)
print(vector)

sumatoria=0
for i in range(len(vector)):
    sumatoria+=pow(vector[i],2)

norma=pow(sumatoria,1/2)
print(f"La norma del vector es {norma}")
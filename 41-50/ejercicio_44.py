# 44. Leer dos vectores, calcular y escribir el ángulo generado entre ellos.

# cos (a) = (u * v)/(|u|*|v|)
# a = cos^-1( (u * v)/(|u|*|v|) )

from math import acos, pi
from funciones import generarVector, normaVector

size=4

vector1=generarVector(size,0,10)
norma1=normaVector(vector1)
print(vector1)

vector2=generarVector(size,0,10)
norma2=normaVector(vector2)
print(vector2)

prodPunto=0
for i in range(size):
    prodPunto+=(vector1[i]*vector2[i])

angulo=acos(prodPunto/(norma1*norma2))/pi*180

print(f"El ángulo entre ambos vectores es {angulo}")
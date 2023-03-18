# 38. Calcular y escribir (de un vector):
# - El valor máximo y el valor mínimo -
# - El promedio -
# - La mediana -
# - La desviación estándar (se asumió una muestra y no una población)
# - La varianza
# Para el máximo y el mínimo, debe calcular además su posición en el vector.

from funciones import generarVector
from ejercicio_34 import organizarVectorAsc

vector=generarVector(20,0,15)
print(vector)

minValor=None
posMin=None
maxValor=None
posMax=None
for i in range(len(vector)):
    if minValor==None or vector[i]<minValor:
        minValor=vector[i]
        posMin=i
    if maxValor==None or vector[i]>maxValor:
        maxValor=vector[i]
        posMax=i

promedio=0
for i in range(len(vector)):
    promedio+=vector[i]
promedio/=len(vector)

vectorOrdenado=organizarVectorAsc(vector)
if len(vectorOrdenado)%2==0:
    mediana=(vectorOrdenado[len(vectorOrdenado)//2]+vectorOrdenado[len(vectorOrdenado)//2-1])/2
else:
    mediana=vectorOrdenado[len(vectorOrdenado)//2]

sumatoria=0
for i in range(len(vector)):
    diferencia=vector[i]-promedio
    sumatoria+=pow(diferencia,2)

desviacion=pow(sumatoria/(len(vector)-1),1/2)
varianza=pow(desviacion,2)


print(f"El valor mínimo es {minValor} y esta en la posición {posMin}")
print(f"El valor máximo es {maxValor} y esta en la posición {posMax}")

print(f"El promedio de los elementos del vector es {promedio}")
print(f"La mediana de los elementos ordenados del vector es {mediana}")
print(f"La desviación estándar de los elementos del vector es {desviacion}")
print(f"La varianza de los elementos del vector es {varianza}")
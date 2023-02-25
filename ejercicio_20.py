# Diseñar un algoritmo que simule el lanzamiento de un dado (usar la función random multiplicada 
# por 6) 500 veces. Calcular y escribir cuántas veces salió cada número (1 a 6).

import random as rd

caras=[0]*6
for i in range(500):
    dado=round(rd.random()*5)+1
    caras[dado-1]+=1

print(caras)

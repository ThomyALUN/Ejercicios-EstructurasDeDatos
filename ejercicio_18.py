# 18. Calcular y escribir la suma de los cuadrados de los impares menores 
# a un número positivo dado.

num=6
suma=0
for i in range(1,num,2):
    suma+=i**2
print(suma)
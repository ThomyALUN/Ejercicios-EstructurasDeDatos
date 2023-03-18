# 8. Diseñar un programa que lea 20 valores y determine y escriba cuál fue el mayor valor
# leído.

#Forma 1: Usando una lista y la función max(). Al final los valores quedan almacenados

""" lista=[]
for i in range(20):
    valor=int(input(f"Ingrese el valor {i+1}: "))
    lista.append(valor)

print(f"El valor máximo fue {max(lista)}.") """

#Forma 2: Los valores no se almacenan pero se conserva el mayor.

""" mayor=None
for i in range(20):
    valor=int(input(f"Ingrese el valor {i+1}: "))
    if mayor==None or valor>mayor:
        mayor=valor

print(f"El valor máximo fue {mayor}.") """
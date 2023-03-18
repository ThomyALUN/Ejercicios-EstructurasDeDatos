# 26. Realizar un algoritmo que lea dos vectores (listas) y encuentre y escriba los elementos
# que sean iguales en los dos.

lista1=[]
lista2=[]

for i in range(10):
    num=float(input(f"Ingrese el valor {i+1} de la lista 1: "))
    lista1.append(num)

for i in range(10):
    num=float(input(f"Ingrese el valor {i+1} de la lista 2: "))
    lista2.append(num)

for i in range(10):
    if lista1[i]==lista2[2]:
        print(f"En la posición {i+1} se repite el elemento {lista1[i]} en ambas listas")
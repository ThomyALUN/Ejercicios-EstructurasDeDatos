# Leer 3 valores, escribirlos en orden ascendente.

vlr1=float(input("Ingrese el primer valor: "))
vlr2=float(input("Ingrese el segundo valor: "))
vlr3=float(input("Ingrese el tercer valor: "))

lista=[vlr1,vlr2,vlr3]
lista.sort()

for valor in lista:
    print(valor)

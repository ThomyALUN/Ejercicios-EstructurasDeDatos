# 21. Leer un valor, calcular y escribir su logaritmo en una base dada. Por ejemplo logaritmo
# en base 2 de 8, debe imprimir 3.

from math import log10

num=int(input("Ingrese la potencia: "))
base=int(input("Ingrese la base: "))
resultado=log10(num)/log10(base)
print(f"Logaritmo en base {base} de {num} es igual a {resultado}")
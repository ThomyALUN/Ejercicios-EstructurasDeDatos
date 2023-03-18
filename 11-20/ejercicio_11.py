# 11. Leer una base real y un exponente entero, implementar y escribir su potencia con sólo multiplicaciones y sumas.

print("Programa que calcula la potencia de un número real con exponente entero")
base=float(input("Ingrese la base: "))
exponente=int(input("Ingrese el exponente: "))
resultado=0
if exponente==0:
    resultado=1
else:
    resultado=base
    for i in range(exponente-1):
        resultado*=base

print(f"{base}^{exponente}={resultado}")

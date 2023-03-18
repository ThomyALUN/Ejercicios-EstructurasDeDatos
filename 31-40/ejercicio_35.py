# 35. Realizar un algoritmo que lea un vector (lista).
# Calcule la diferencia más grande entre 2 elementos consecutivos de este vector.

vector=[]
tamanio=int(input("Ingrese el tamaño del vector: "))

for i in range(tamanio):
    num=float(input("Ingrese un valor: "))
    vector.append(num)

maxDif=0
for i in range(tamanio-1):
    resta=abs(vector[i]-vector[i+1])
    if resta>maxDif:
        maxDif=resta

print(f"La diferencia más grande entre dos números consecutivos es: {maxDif}")
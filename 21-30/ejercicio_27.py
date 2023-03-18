# 27. Calcular el número de elementos positivos, negativos y cero de un vector (lista) dado.

lista=[10,0,2,-4,2,0,-5,30,100,20,-20,0,4]

pos=0
neg=0
cero=0

for i in range(len(lista)):
    valor=lista[i]
    if valor==0:
        cero+=1
    elif valor>0:
        pos+=1
    else:
        neg+=1

print(f"La lista tiene {cero} ceros")
print(f"La lista tiene {pos} valores positivos")
print(f"La lista tiene {neg} valores negativos")
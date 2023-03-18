# 25. Realizar un algoritmo que lea un vector (lista). Conformar un segundo vector (lista) que
# contenga los elementos positivos y otro que contenga los elementos negativos del vector
# (lista) inicial. Escribir todos los vectores generados.

listaInicial=[]

for i in range(10):
    num=int(input("Ingrese un valor: "))
    listaInicial.append(num)

listaPos=[]
listaNeg=[]
for i in range(10):
    if listaInicial[i]>0:
        listaPos.append(listaInicial[i])
    elif listaInicial[i]<0:
        listaNeg.append(listaInicial[i])

print(f"La lista inicial es: {listaInicial}")
print(f"La lista positiva es: {listaPos}")
print(f"La lista negativa es: {listaNeg}")
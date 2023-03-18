# 13. Diseñar un algoritmo que encuentre el entero positivo más pequeño (num) 
# para el cual la suma 1 + 2 + 3 + .... + num es mayor que un límite dado (lim).

lim=int(input("Ingrese el valor límite: "))
contador=0
acumulador=0
while True:
    contador+=1
    acumulador+=contador
    print(contador,end=" ")
    if acumulador>lim:
        break
    print("+",end=" ")
print(f"= {acumulador}")

print(f"\nnum = {contador}")
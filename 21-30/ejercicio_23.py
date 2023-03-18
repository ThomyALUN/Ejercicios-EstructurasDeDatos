# 23. Diseñar programa que lea un número dado no mayor de 9 y genere y escriba el siguiente
# triángulo hasta ese número.
# 1
# 121
# 12321
# 1234321
# 123454321
# .....

renglones=int(input("Ingrese la cantidad de filas que desea imprimir: "))
for i in range(renglones):
    contador=0
    sumador=1
    for j in range(i*2+1):
        contador+=sumador
        print(contador,end="")
        if j==(i*2)//2:
            sumador=-1
    print("")
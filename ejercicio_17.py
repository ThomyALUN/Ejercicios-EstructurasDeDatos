# 17. Calcular y escribir los primeros 150 números de Fibonacci.

num1=0
num2=1
print(num1)
print(num2)

cantidad=2

while cantidad<150:
    cantidad+=1
    aux=num1+num2   #Resultado de la suma de los elementos actuales
    num1=num2       #Se mueve el segundo término a la posición del primero
    num2=aux        #Se mueve el resultado al segundo término
    print(num2)


#Se calculan 2 términos a la vez
"""
while cantidad<150:
    cantidad+=2

    aux1=num1+num2
    aux2=aux1+num2

    num1=aux1
    num2=aux2

    print(num1)
    print(num2)
"""
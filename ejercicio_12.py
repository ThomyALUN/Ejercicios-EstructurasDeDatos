# 12. Leer dos números enteros, calcular y escribir su producto, usando sólo sumas y/o restas.

num1=int(input("Ingrese el primer valor: "))
num2=int(input("Ingrese el segundo valor: "))

resultado=0
if (num1>=0 and num2>=0) or (num1<0 and num2<0):
    for i in range(abs(num1)):
        resultado+=abs(num2)
elif num1>0 and num2<0:
    for i in range(num1):
        resultado+=num2
else:
    for i in range(num2):
        resultado+=num1

print(resultado)
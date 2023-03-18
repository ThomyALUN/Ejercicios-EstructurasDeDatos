# 24. Diseñar un algoritmo que lea un valor X (dado en radianes) y calcule el valor de la función
# trigonométrica seno así:
# sen x = x/1! – x^3/3! + x^5/5!+ .....

# La fórmula sería: x^(2n-1)/(2n-1)! * (-1)^(n+1)

from math import factorial
from decimal import Decimal

iteraciones=100

radianes=float(input("Ingrese el valor del ángulo en radianes cuyo valor desea calcular: "))

sumatoria=Decimal(0)
for i in range(1,iteraciones+1):
    sumatoria+=Decimal(Decimal(pow(radianes,2*i-1))/Decimal(factorial(2*i-1))*Decimal(pow(-1,i+1)))

print(f"El seno de {radianes} rad es {sumatoria}")
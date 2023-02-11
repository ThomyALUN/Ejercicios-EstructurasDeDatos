# Calcular y escribir el valor de pi, dado por la serie:
# 4(1-1/3+1/5-1/7+1/9-1/11+ …)

n=int(input("Ingrese la cantidad de valores que desea calcular de la serie de pi: "))
suma=0
for i in range(n):
    #La fórmula es (-1)^n*(1/2n+1). n comienza en 0
    suma=suma+pow(-1,(n))*(1/(2*n+1))
suma=suma*4

print(f"El valor aproximado de pi con {n} valores en la sumatoria de Leibniz es de {suma}")
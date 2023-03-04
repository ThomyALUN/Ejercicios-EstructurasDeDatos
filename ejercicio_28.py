# 28. Leer los coeficientes de un polinomio de grado n, calcular su derivada.

n=int(input("Ingrese el grado del polinomio: "))

coefFuncion=[]
coefDerivada=[]

for i in range(n+1):
    valor=float(input(f"Ingrese del valor del término de grado {n-i}: "))
    coefFuncion.append(valor)

print("\nLa función es: ", end="")
for i in range(n+1):
    print(f"{coefFuncion[i]}*x^{n-i}",end="")
    if i<n:
        print(" + ", end="")

for i in range(n):
    valor=coefFuncion[i]*(n-i)
    coefDerivada.append(valor)

gradoDerivada=n-1
print("\nLa derivada es: ", end="")
for i in range(gradoDerivada+1):
    print(f"{coefDerivada[i]}*x^{n-i}",end="")
    if i<(gradoDerivada):
        print(" + ", end="")
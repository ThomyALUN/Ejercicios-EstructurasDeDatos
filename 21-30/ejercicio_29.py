# 29. Leer los coeficientes de un polinomio de grado n, calcular su integral entre dos límites dados.

n=int(input("Ingrese el grado del polinomio: "))

lim=[2,4]
coefFuncion=[]
coefIntegral=[]

for i in range(n+1):
    valor=float(input(f"Ingrese del valor del término de grado {n-i}: "))
    coefFuncion.append(valor)

print("\nLa función es: ", end="")
for i in range(n+1):
    print(f"{coefFuncion[i]}*x^{n-i}",end="")
    if i<n:
        print(" + ", end="")

for i in range(n+1):
    exponenteViejo=n-i                  #Exponente actual
    exponenteNuevo=exponenteViejo+1     #Exponente luego de adicionar 1
    valor=coefFuncion[i]/exponenteNuevo
    coefIntegral.append(valor)

gradoIntegral=n+1
print("\nLa integral indefinida es: ", end="")
for i in range(gradoIntegral):
    exponente=n-i+1
    print(f"{coefIntegral[i]}*x^{n-i+1}",end="")
    if i<(gradoIntegral):
        print(" + ", end="")
print("C")

suma=0
#Cálculo límite inferior
for i in range(gradoIntegral):
    exponente=n-i+1
    coeficiente=coefIntegral[i]
    valor=coeficiente*pow(lim[0],exponente)
    suma-=valor

#Cálculo límite superior
for i in range(gradoIntegral):
    exponente=n-i+1
    coeficiente=coefIntegral[i]
    valor=coeficiente*pow(lim[1],exponente)
    suma+=valor

print(f"El resultado de la integral definida entre {lim[0]} y {lim[1]} es: {suma}")
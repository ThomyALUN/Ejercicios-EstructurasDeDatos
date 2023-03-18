# 33. Leer dos vectores (listas), calcular y escribir el producto punto de ambos.


vector1=[]
vector2=[]
vectorMult=[]

tamanio=int(input("Ingrese el tamaño de los vectores: "))

for i in range(tamanio):
    num=float(input(f"Ingrese el valor {i+1} del vector 1: "))
    vector1.append(num)

for i in range(tamanio):
    num=float(input(f"Ingrese el valor {i+1} del vector 2: "))
    vector2.append(num)

for i in range(tamanio):
    vectorMult.append(vector1[i]*vector2[i])

print(f"El vector resultante es: {vectorMult}")
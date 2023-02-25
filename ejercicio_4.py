# 4. Leer las coordenadas (x, y) de un punto en el plano cartesiano, determinar y escribir a qué
# cuadrante pertenece basado en el signo, de acuerdo con el gráfico mostrado.

x=float(input("Ingrese el valor de la coordenada X: "))
y=float(input("Ingrese el valor de la coordenada Y: "))

if x==0:
    if y==0:
        print("El punto esta en el origen.")
    elif y>0:
        print("El punto esta sobre el eje Y positivo.")
    else:
        print("El punto esta sobre el eje Y negativo.")
elif x>0:
    if y==0:
        print("El punto esta sobre el eje X positivo.")
    elif y>0:
        print("El punto esta en el primer cuadrante.")
    else:
        print("El punto esta en el cuarto cuadrante.")
else:               #x<0
    if y==0:
        print("El punto esta sobre el eje X negativo.")
    elif y>0:
        print("El punto esta en el segundo cuadrante.")
    else:
        print("El punto esta en el tercer cuadrante.")
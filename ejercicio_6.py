# 6. Leer un ángulo en grados determinar y escribir a qué cuadrante pertenece.

angulo=float(input("Ingrese un ángulo: "))
anguloMod=angulo%360    #Se saca el módulo para que los ángulos menores a 0° o mayores a 360° se traten como múltiplos

if anguloMod%90==0:
    if anguloMod//90==0:
        print("El ángulo apunta al eje X positivo.")
    elif anguloMod//90==1:
        print("El ángulo apunta al eje Y positivo.")
    elif anguloMod//90==2:
        print("El ángulo apunta al eje X negativo.")
    else:
        print("El ángulo apunta al eje Y negativo.")
else:
    cuadrante=int(anguloMod//90+1)
    print(f"El ángulo {angulo}° se encuentra en el cuadrante {cuadrante}.")
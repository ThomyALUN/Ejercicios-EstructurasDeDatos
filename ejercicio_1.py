from math import acos, pi

# Ejercicio #1: Leer tres valores, determinar si corresponden a los lados de un triángulo. Si es así, calcular
# y escribir el perímetro si el triángulo es rectángulo o su área, en otro caso.

l1=float(input("Ingrese el tamaño del primer lado: "))
l2=float(input("Ingrese el tamaño del segundo lado: "))
l3=float(input("Ingrese el tamaño del tercer lado: "))
print("")

if l1>0 and l2>0 and l3>0:
    try:
        angulo_1=acos((pow(l1,2)-pow(l2,2)-pow(l3,2))/(-2*l2*l3))*(180/pi)
        angulo_2=acos((pow(l2,2)-pow(l1,2)-pow(l3,2))/(-2*l1*l3))*(180/pi)
        angulo_3=acos((pow(l3,2)-pow(l1,2)-pow(l2,2))/(-2*l1*l2))*(180/pi)
    except ValueError:
        print("Los lados del triángulo son inválidos. No se puede continuar con los cálculos.")
        exit()
    sumaAngulos=round(angulo_1+angulo_2+angulo_3)
    if angulo_1>0 and angulo_2>0 and angulo_3>0 and sumaAngulos==180:
        print("Los lados del triángulo son válidos. Se procederá a realizar el cálculo correspondiente.")
        print(f"Los ángulos del triángulo son: {angulo_1:.2f}, {angulo_2:.2f}, {angulo_3:.2f} respectivamente")
        perimetro=l1+l2+l3
        if angulo_1==90 or angulo_2==90 or angulo_3==90:
            print(f"El triángulo es rectángulo y su perimetro es de {perimetro} unidades.")
        else:
            area=perimetro*(perimetro-l1)*(perimetro-l2)*(perimetro-l3)
            area=pow(area,1/2)
            print(f"El triángulo no es rectángulo y su área es de {area} unidades cuadradas.")
    else:
        print("Los lados del triángulo son inválidos. No se puede continuar con los cálculos.")
else:
    print("Al menos uno de los lados vale 0 o es un número negativo. No se puede continuar con los cálculos.")

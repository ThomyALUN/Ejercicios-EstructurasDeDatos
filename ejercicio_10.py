# Diseñar un algoritmo que convierta una temperatura dada en una escala a temperatura en 
# otra escala que se pida.
# La relación entre las diferentes escalas de temperaturas está dada por la siguiente relación:
# C/5 = R/4 = (F - 32) / 9
# Siendo C=Celsius, R= Reamur, F=Fahrenheit

print("***BIENVENIDO AL SISTEMA DE CONVERSIÓN DE TEMPERATURA***")
print("1. Celsius a Reamur")
print("2. Celsius a Fahrenheit")
print("3. Reamur a Celsius")
print("4. Reamur a Fahrenheit")
print("5.Fahrenheit a Celsius")
print("6.Fahrenheit a Reamur\n")

opcion=int(input("Ingrese el número de la opción que desea utilizar: "))
if opcion==1:
    C=float(input("\nIngrese el valor de la temperatura en grados Celsius: "))
    R=4/5*C
    print(f"Al convertir {C}° Celsius se obtienen {R:.2f}° Reamur.")
elif opcion==2:
    C=float(input("\nIngrese el valor de la temperatura en grados Celsius: "))
    F=(9/5*C)+32
    print(f"Al convertir {C}° Celsius se obtienen {F:.2f}° Fahrenheit.")
elif opcion==3:
    R=float(input("\nIngrese el valor de la temperatura en grados Reamur: "))
    C=5/4*R
    print(f"Al convertir {R}° Reamur se obtienen {C:.2f}° Celsius.")
elif opcion==4:
    R=float(input("\nIngrese el valor de la temperatura en grados Reamur: "))
    F=(9/4*R)+32
    print(f"Al convertir {R}° Reamur se obtienen {F:.2f}° Fahrenheit.")
elif opcion==5:
    F=float(input("\nIngrese el valor de la temperatura en grados Fahrenheit: "))
    C=5/9*(F-32)
    print(f"Al convertir {F}° Fahrenheit se obtienen {C:.2f}° Celsius.")
elif opcion==6:
    F=float(input("\nIngrese el valor de la temperatura en grados Fahrenheit: "))
    R=4/9*(F-32)
    print(f"Al convertir {F}° Fahrenheit se obtienen {R:.2f}° Reamur.")
else:
    print("Ha ingresado un valor inválido. Se terminará el programa.")
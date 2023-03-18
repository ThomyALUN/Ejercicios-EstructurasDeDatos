# 14. Diseñar un algoritmo que lea un valor correspondiente a un mes y valide si es correcto,
# de lo contrario se debe escribir que es incorrecto y se debe volver a leer hasta que se entre
# bien. Cuando se haya leído bien el mes, se debe escribir el nombre del mes.

try:
    while True:
        valor=int(input("Ingrese el mes: "))
        if valor<1 or valor>12:
            print(f"{valor} no es un mes válido. Debe ingresar un nuevo valor.\n")
        else:
            if valor==1:
                mes="enero"
            elif valor==2:
                mes="febrero"
            elif valor==3:
                mes="marzo"
            elif valor==4:
                mes="abril"
            elif valor==5:
                mes="mayo"
            elif valor==6:
                mes="junio"
            elif valor==7:
                mes="julio"
            elif valor==8:
                mes="agosto"
            elif valor==9:
                mes="septiembre"
            elif valor==10:
                mes="octubre"
            elif valor==11:
                mes="noviembre"
            else:
                mes="diciembre"
            print(f"El mes es {mes}")

except TypeError:
    print("Ingresó un valor inválido como número")
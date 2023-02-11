# Leer el nombre, el peso y la talla de una persona, calcular su índice de masa corporal.
# Determinar y escribir si está en estado de bajo peso, normal, sobrepreso, u obesidad.

nombre=input("Ingrese su nombre: ")
peso=float(input("Ingrese su peso en kgs: "))
talla=float(input("Ingrese su altura en mts: "))

if len(nombre)>0 and peso>0 and talla>0:
    imc=peso/(talla*talla)
    if imc<18.5:
        print(f"{nombre}, usted se encuentra con insuficiencia ponderal. (Bajo/baja de peso)")
    elif imc<25:
        print(f"{nombre}, usted se encuentra en el intervalo normal de peso.")
    elif imc<30:
        print(f"{nombre}, usted se encuentra en el intervalo de preobesidad. (sobrepeso)")
    elif imc<35:
        print(f"{nombre}, usted se encuentra en un estado de obesidad de clase I.")
    elif imc<40:
        print(f"{nombre}, usted se encuentra en un estado de obesidad clase II.")
    else:
        print(f"{nombre}, usted se encuentra en un estado de obesidad de clase III.")
else:
    print("Alguno de los datos ingresados es inválido. Se terminará la ejecución del programa.")
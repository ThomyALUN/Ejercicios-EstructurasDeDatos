# 50. Dado un valor entre 0 y 100. Escribirlo en letras. 
# Por ejemplo 43, debe escribir cuarenta y tres.

especiales={
    "11":"once",
    "12":"doce",
    "13":"trece",
    "14":"catorce",
    "15":"quince"
}

unidades={
    "1":"uno",
    "2":"dos",
    "3":"tres",
    "4":"cuatro",
    "5":"cinco",
    "6":"seis",
    "7":"siete",
    "8":"ocho",
    "9":"nueve"
}

decenas={
    "1":"diez",
    "2":"veinte",
    "3":"treinta",
    "4":"cuarenta",
    "5":"cincuenta",
    "6":"sesenta",
    "7":"setenta",
    "8":"ochenta",
    "9":"noventa"
}

num=input("Ingrese un número de 0 a 100: ")

if int(num)<0 or int(num)>100:
    exit()

print(f"{num} lee como ",end="")
if num=="100":
    print("Cien")
else:
    if num in especiales.keys():
        print(especiales[num])
    else:
        if len(num)==2:
            valorDecena=num[0]
            valorUnidad=num[1]
            print(decenas[valorDecena], end="")
            if valorUnidad!=0:
                print(f" y {unidades[valorUnidad]}")
        else:
            valorUnidad=num[0]
            print(unidades[valorUnidad], end="")
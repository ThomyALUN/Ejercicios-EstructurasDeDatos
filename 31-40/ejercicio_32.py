# 32. Leer una fecha como mes y día, determinar si es una fecha válida. 
# Por ejemplo 30 de febrero debería escribir que no es válida.

limMes={
    "01":31,
    "02":29,
    "03":31,
    "04":30,
    "05":31,
    "06":30,
    "07":31,
    "08":31,
    "09":30,
    "10":31,
    "11":30,
    "12":31
}

fecha=input("Ingrese una fecha en formato MMDD: ")
mes=fecha[:2]
dia=int(fecha[2:])

print(f"El mes ingresado es {mes}")
print(f"El dia ingresado es {dia}")

if dia<=0 or dia>limMes[mes]:
    print("Esta fecha es inválida")
else:
    print("Esta fecha es válida")

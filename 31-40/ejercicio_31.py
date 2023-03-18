# 31. Leer una fecha en formato numérico AAAAMMDD, lo escriba como DD de mes de AAAA. 
# Por ejemplo, 20130419 debe escribir 19 de Abril de 2013.

fecha=input("Ingrese una fecha en formato AAAAMMDD: ")
dia=fecha[-2:]
numMes=fecha[-4:-2]
anio=fecha[:4]

textoMes={
    "01":"enero",
    "02":"febrero",
    "03":"marzo",
    "04":"abril",
    "05":"mayo",
    "06":"junio",
    "07":"julio",
    "08":"agosto",
    "09":"septiembre",
    "10":"octubre",
    "11":"noviembre",
    "12":"diciembre"
}

print(f"La fecha es {dia} de {textoMes[numMes]} de {anio}")
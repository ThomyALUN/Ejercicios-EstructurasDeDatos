# Leer el consumo en metros cúbicos de agua de una familia, calcular y escribir el valor de
# su factura, teniendo en cuenta lo siguiente: los primeros 20 metros cúbicos se cobran
# $2000, los siguientes 6 a $2500 y los restantes a $4.000. Así, por ejemplo, una familia que
# consuma 35 m3, pagaría 20 en la primera tarifa, 6 en la segunda y el resto (9) en la última
# tarifa.

consumo=int(input("Ingrese el consumo de agua en m3: "))

if consumo<=20:
    tarifa=consumo*2000
elif consumo<=26:
    tarifa=(20*2000)+(consumo-20)*2500
else:
    tarifa=(20*2000)+(6*2500)+(consumo-26)*4000

print(f"La tarifa a pagar es de {tarifa}")
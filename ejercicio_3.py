# 3. Leer 3 valores, escribirlos en orden ascendente.

vlr1=float(input("Ingrese el primer valor: "))
vlr2=float(input("Ingrese el segundo valor: "))
vlr3=float(input("Ingrese el tercer valor: "))

lista=[vlr1,vlr2,vlr3]
lista.sort()

print("\nMétodo #1\n")
for valor in lista:
    print(valor)

print("\nMétodo #2\n")

if vlr1==vlr2:
    if vlr1==vlr3:
        print(f"{vlr1}\n{vlr1}\n{vlr1}")
    elif vlr1>vlr3:
        print(f"{vlr3}\n{vlr1}\n{vlr1}")
    else: #vlr1<vlr3
        print(f"{vlr1}\n{vlr1}\n{vlr3}")
elif vlr1==vlr3:
    if vlr1>vlr2:
        print(f"{vlr2}\n{vlr1}\n{vlr1}")
    else: #vlr1<vlr2
        print(f"{vlr1}\n{vlr1}\n{vlr2}")
elif vlr2==vlr3:
    if vlr2>vlr1:
        print(f"{vlr1}\n{vlr2}\n{vlr2}")
    else:
        print(f"{vlr2}\n{vlr2}\n{vlr1}")
elif vlr1>vlr2:
    if vlr2>vlr3:
        print(f"{vlr3}\n{vlr2}\n{vlr1}")
    else:   #vlr2<vlr3
        if vlr1>vlr3:
            print(f"{vlr2}\n{vlr3}\n{vlr1}")
        else:   #vlr1<vlr3
            print(f"{vlr2}\n{vlr1}\n{vlr3}")
else:   #vlr2>vlr1
    if vlr1>vlr3:
        print(f"{vlr3}\n{vlr1}\n{vlr2}")
    else:   #vlr3>vlr1
        if vlr2>vlr3:
            print(f"{vlr1}\n{vlr3}\n{vlr2}")
        else:   #vlr3>vlr2
            print(f"{vlr1}\n{vlr2}\n{vlr3}")

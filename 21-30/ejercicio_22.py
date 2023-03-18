# 22. Leer una fecha en formato numérico AAAAMMDD, lo escriba como AAAA/MM/DD.
# Por ejemplo, 20200601 debe escribir 2020/06/01.

date=input("Ingrese una fecha en formato AAAAMMDD: ")
year=date[:4]
month=date[4:6]
day=date[6:]

print(f"La fecha ingresada es {year}/{month}/{day}")
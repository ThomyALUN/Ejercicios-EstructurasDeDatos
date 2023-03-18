# 5. Diseñar un algoritmo que imprima las tablas de multiplicar hasta el 9

for i in range(1,10):
    print(f"Tabla de multiplicar del {i}")
    for j in range(1,11):
        print(f"{i} * {j} = {i*j}")
    print("")
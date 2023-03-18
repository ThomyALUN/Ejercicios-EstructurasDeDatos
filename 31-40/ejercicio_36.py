# 36. Crear y escribir un vector (lista) de 20 elementos.
# Asignar a cada elemento un valor igual al negativo del inverso de la posición que ocupa. i -> -1/i

vector=[]
for i in range(20):
    try:
        vector.append(-1/i)
    except:
        vector.append(0)

print(vector)
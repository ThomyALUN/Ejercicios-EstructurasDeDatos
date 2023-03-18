# 49. Leer 2 vectores que representen conjuntos. 
# Diseñar los métodos que calculen y escriban el conjunto unión, el conjunto intersección. 
# Debe tenerse en cuenta que los conjuntos no tienen elementos repetidos.

from funciones import generarVectorNoRpt

def union(conjunto1, conjunto2):
    cjtoUnion=[]
    for i in range(len(conjunto1)):
        if conjunto1[i] not in cjtoUnion:
            cjtoUnion.append(conjunto1[i])
    for i in range(len(conjunto2)):
        if conjunto2[i] not in cjtoUnion:
            cjtoUnion.append(conjunto2[i])
    return cjtoUnion

def interseccion(conjunto1, conjunto2):
    cjtoInter=[]
    for i in range(len(conjunto1)):
        if conjunto1[i] in conjunto2 and conjunto1[i] not in cjtoInter:
            cjtoInter.append(conjunto1[i])
    return cjtoInter

conjunto1=generarVectorNoRpt(5,0,20)
conjunto2=generarVectorNoRpt(5,0,20)
print(conjunto1)
print(conjunto2)

print(union(conjunto1, conjunto2))
print(interseccion(conjunto1, conjunto2))
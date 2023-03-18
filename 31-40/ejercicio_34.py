# 34. Realizar un algoritmo que lea un vector (lista) y genere un nuevo vector ordenado descendentemente.

def organizarVectorDesc(vector):
    nuevoVector=vector[:]
    for i in range(0,len(nuevoVector)-1):
        for j in range(0,len(nuevoVector)-i-1):
            if nuevoVector[j]<nuevoVector[j+1]:
                aux=nuevoVector[j]
                nuevoVector[j]=nuevoVector[j+1]
                nuevoVector[j+1]=aux
    return nuevoVector

def organizarVectorAsc(vector):
    nuevoVector=vector[:]
    for i in range(0,len(nuevoVector)-1):
        for j in range(0,len(nuevoVector)-i-1):
            if nuevoVector[j]>nuevoVector[j+1]:
                aux=nuevoVector[j]
                nuevoVector[j]=nuevoVector[j+1]
                nuevoVector[j+1]=aux
    return nuevoVector

if __name__=="__main__":
    vector=[2, 3, 1, 5, 2, 62, 5, 6]
    nuevoVector=organizarVectorDesc(vector)
    print(nuevoVector)
    nuevoVector=organizarVectorAsc(vector)
    print(nuevoVector)
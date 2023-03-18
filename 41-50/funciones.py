from random import randint

def generarVector(size, limInf, limSup):
    vector=[]
    for i in range(size):   
        vector.append(randint(limInf,limSup))
    return vector

def generarVectorNoRpt(size, limInf, limSup):
    if size>(limSup-limInf):
        return None
    while True:
        vector=[]
        for i in range(size):   
            vector.append(randint(limInf,limSup))
        vectorNoRept=eliminarRptds(vector)
        if len(vectorNoRept)==size:
            break
    return vectorNoRept

def eliminarRptds(vector):
    vectorNoRept=[]
    for i in range(len(vector)):
        if vector[i] not in vectorNoRept:
            vectorNoRept.append(vector[i])
    return vectorNoRept

def normaVector(vector):
    sumatoria=0
    for i in range(len(vector)):
        sumatoria+=pow(vector[i],2)
    norma=pow(sumatoria,1/2)
    return norma
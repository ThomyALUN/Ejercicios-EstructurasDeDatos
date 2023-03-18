from random import randint

def generarVector(size, limInf, limSup):
    vector=[]
    for i in range(size):   
        vector.append(randint(limInf,limSup))
    return vector
# 45. Leer dos vectores (listas): uno, contiene los códigos de los estudiantes que perdieron Matemáticas.
# El otro, contiene los códigos de los estudiantes que perdieron Física. 
# Generar y escribir un nuevo vector de los códigos de los estudiantes que perdieron Matemáticas y Física.

from funciones import generarVectorNoRpt

size=10

docsMath=generarVectorNoRpt(size,0,50)
print(docsMath)

docsFisica=generarVectorNoRpt(size,0,100)
print(docsFisica)

docsAmbas=[]

for i in range(size):
    estudiante=docsMath[i]
    if estudiante in docsFisica and estudiante not in docsAmbas:
        docsAmbas.append(estudiante)

print(docsAmbas)

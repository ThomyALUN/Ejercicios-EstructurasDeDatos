# 30. Se tienen dos vectores (listas). Se debe crear otros 3 vectores. El primero, 
# con la suma de los elementos respectivos, otro con el producto y el último con 
# la diferencia (si la diferencia es negativa, coloque cero como valor).

lista1=[20,3,1,4,6]
lista2=[5,0,4,3,2]

suma=[]
producto=[]
diferencia=[]

#Suma
for i in range(len(lista1)):
    valor=lista1[i]+lista2[i]
    suma.append(valor)

#Producto
for i in range(len(lista1)):
    valor=lista1[i]*lista2[i]
    producto.append(valor)

#Diferencia
for i in range(len(lista1)):
    valor=lista1[i]-lista2[i]
    if valor<0:
        diferencia.append(0)
    else:
        diferencia.append(valor)

print(suma)
print(producto)
print(diferencia)

# 15. Calcular y escribir los primeros 100 números primos.

from math import sqrt, ceil

primos=0
num=1
while primos<100:
	num+=1
	raiz=sqrt(num)
	
	if raiz%1==0:
		raiz=int(raiz)
	else:
		raiz=ceil(raiz)
	
	primo=True
	if num!=2:
		for divisor in range(2,raiz+1):
			if num%divisor==0:
				primo=False

	if primo: 
		primos+=1
		print(f"¿El número {num} es primo?: {primo}")

print(f"Se han encontrado {primos} números primos")
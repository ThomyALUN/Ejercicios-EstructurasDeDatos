# 19. Generar y escribir el valor del seno de 0 a 360 grados, en incrementos de 5 grados.

from math import sin,pi

for angulo in range(0,361,5):
    radianes=angulo/180*pi
    senoAngulo=sin(radianes)
    print(angulo, radianes, senoAngulo)
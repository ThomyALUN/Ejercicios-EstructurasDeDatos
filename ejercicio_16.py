# 16. Diseñar un algoritmo que lea las notas de Matemáticas y Física de un grupo de 25
# estudiantes. Determinar y escribir cuántos ganaron las dos y cuántos perdieron al menos
# una.

perdieron=0
ganaron2=0
for i in range(25):
    mate=float(input(f"Ingrese la nota de matemáticas del estudiante {i+1}: "))
    fisica=float(input(f"Ingrese la nota de física del estudiante {i+1}: "))
    print(f"Mate:{mate},Física:{fisica}")
    if mate>=3 and fisica>=3:
        ganaron2+=1
        continue
    elif mate<3 or fisica<3:
        perdieron+=1

print(f"{ganaron2} estudiantes ganaron ambas asignaturas.")
print(f"{perdieron} perdieron al menos una asignatura")